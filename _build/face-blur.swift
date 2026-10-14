// Soft face blur for photographs of players who have not given consent (Andrew, 14 Oct 2026:
// "light and clean", not a mosaic or a sticker). macOS only: Vision finds the faces, Core Image
// blurs inside a feathered ellipse, so the edge cannot be seen and hair, hands and instruments
// stay sharp.
//
//   swiftc -O _build/face-blur.swift -o /tmp/face-blur
//   /tmp/face-blur faces <photo>                      size and face boxes (pixels, top left origin)
//   /tmp/face-blur blur <photo> <out.jpg> x,y,w[,h] …  blur these faces (boxes as `faces` prints them,
//                                                      brow to chin; add a box by hand for a face
//                                                      Vision missed, such as a profile or a half face)
//   /tmp/face-blur crop <photo> <out.jpg> x y w h      exact crop
//
// Then run the result through _build/add-photo.sh like any photograph, add it to
// _build/photos.py as "blurred", and look at every face at full size before publishing.
// The strength (sigma = 0.075 of the ellipse width) left 50 to 200 pixel faces with no
// features while the photograph still reads as soft focus; 0.06 to 0.12 were compared.
import Foundation
import CoreImage
import CoreImage.CIFilterBuiltins
import Vision

let ctx = CIContext(options: [.workingColorSpace: CGColorSpace(name: CGColorSpace.sRGB)!])

func load(_ p: String) -> CIImage {
    guard let im = CIImage(contentsOf: URL(fileURLWithPath: p), options: [.applyOrientationProperty: true]) else {
        FileHandle.standardError.write("cannot read \(p)\n".data(using: .utf8)!); exit(1)
    }
    return im.transformed(by: CGAffineTransform(translationX: -im.extent.origin.x, y: -im.extent.origin.y))
}

func save(_ im: CIImage, _ out: String) {
    let key = CIImageRepresentationOption(rawValue: kCGImageDestinationLossyCompressionQuality as String)
    try! ctx.writeJPEGRepresentation(of: im, to: URL(fileURLWithPath: out),
                                     colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!, options: [key: 0.95])
}

let a = CommandLine.arguments
guard a.count > 2 else { print("face-blur faces|blur|crop …  (see the head of this file)"); exit(1) }
let im = load(a[2])
let W = im.extent.width, H = im.extent.height

switch a[1] {
case "faces":
    let req = VNDetectFaceRectanglesRequest()
    try! VNImageRequestHandler(ciImage: im).perform([req])
    print("\(Int(W)) x \(Int(H))")
    for f in req.results ?? [] {
        let b = f.boundingBox
        print(String(format: "%.0f,%.0f,%.0f,%.0f   (confidence %.2f)",
                     b.minX * W, (1 - b.maxY) * H, b.width * W, b.height * H, f.confidence))
    }

case "blur":
    var out = im
    for box in a[4...] {
        let v = box.split(separator: ",").map { CGFloat(Double($0)!) }
        let x = v[0], y = v[1], w = v[2], h = v.count > 3 ? v[3] : v[2]
        // the ellipse: wider and taller than the face box, lifted to take the forehead, not the neck
        let ew = 1.55 * w, eh = 1.85 * h
        let cx = x + w / 2, cy = H - (y + h / 2 - 0.12 * h)          // Core Image counts from the bottom
        let blurred = out.clampedToExtent().applyingGaussianBlur(sigma: Double(0.075 * ew)).cropped(to: im.extent)
        let g = CIFilter.radialGradient()                              // solid inside 70%, nothing at the edge
        g.center = .zero
        g.radius0 = Float(ew / 2 * 0.70); g.radius1 = Float(ew / 2)
        g.color0 = CIColor(red: 1, green: 1, blue: 1); g.color1 = CIColor(red: 0, green: 0, blue: 0)
        let mask = g.outputImage!
            .transformed(by: CGAffineTransform(scaleX: 1, y: eh / ew))
            .transformed(by: CGAffineTransform(translationX: cx, y: cy))
            .cropped(to: im.extent)
        let m = CIFilter.blendWithMask()
        m.inputImage = blurred; m.backgroundImage = out; m.maskImage = mask
        out = m.outputImage!.cropped(to: im.extent)
    }
    save(out, a[3])

case "crop":
    let x = CGFloat(Double(a[4])!), y = CGFloat(Double(a[5])!), w = CGFloat(Double(a[6])!), h = CGFloat(Double(a[7])!)
    let r = CGRect(x: x, y: H - y - h, width: w, height: h)
    save(im.cropped(to: r).transformed(by: CGAffineTransform(translationX: -r.minX, y: -r.minY)), a[3])

default:
    print("face-blur faces|blur|crop …  (see the head of this file)"); exit(1)
}
