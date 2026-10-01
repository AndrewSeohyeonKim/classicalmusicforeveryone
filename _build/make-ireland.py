#!/usr/bin/env python3
# Regenerates _build/geo_ireland.py (run once; the output is checked in).
#   curl -o /tmp/ne10.geojson https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_0_countries.geojson
#   python3 _build/make-ireland.py /tmp/ne10.geojson _build/geo_ireland.py 1.15 60
"""One outline for the island of Ireland from Natural Earth 1:10m admin-0: the
Republic and Northern Ireland dissolved into a single ring (their shared
border edges removed and the rest chained back together), small islands
dropped, simplified with Ramer-Douglas-Peucker in viewBox units."""
import json, math, sys
SRC, OUT = sys.argv[1], sys.argv[2]
EPS = float(sys.argv[3]) if len(sys.argv) > 3 else 0.9
MIN_KM2 = float(sys.argv[4]) if len(sys.argv) > 4 else 60
H = 400.0
LAT0, LAT1, LON0, LON1 = 51.36, 55.44, -10.72, -5.38
K = math.cos(math.radians(53.5)); SC = H / (LAT1 - LAT0); W = (LON1 - LON0) * K * SC
def proj(lon, lat): return ((lon - LON0) * K * SC, (LAT1 - lat) * SC)
d = json.load(open(SRC))
rings = []
for ft in d["features"]:
    if ft["properties"].get("ADM0_A3") not in ("IRL", "GBR"): continue
    g = ft["geometry"]
    for p in (g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]):
        r = p[0]
        if all(-11 < x < -5 and 51 < y < 55.6 for x, y in r): rings.append(r)
def k(a): return (round(a[0], 6), round(a[1], 6))
# count undirected edges
cnt = {}
for r in rings:
    for i in range(len(r) - 1):
        e = tuple(sorted((k(r[i]), k(r[i + 1])))); cnt[e] = cnt.get(e, 0) + 1
# directed edges that are not shared
nxt = {}
for r in rings:
    for i in range(len(r) - 1):
        a, b = k(r[i]), k(r[i + 1])
        if cnt[tuple(sorted((a, b)))] == 1:
            nxt.setdefault(a, []).append(b)
# chain into rings
out_rings = []
while nxt:
    start = next(iter(nxt)); ring = [start]; cur = start
    while True:
        b = nxt[cur].pop()
        if not nxt[cur]: del nxt[cur]
        ring.append(b); cur = b
        if cur == start or cur not in nxt: break
    out_rings.append(ring)
def area_km2(r):
    s = 0
    for i in range(len(r) - 1):
        (x1, y1), (x2, y2) = r[i], r[i + 1]
        s += (x1 * K * 111.32) * (y2 * 110.57) - (x2 * K * 111.32) * (y1 * 110.57)
    return abs(s) / 2
def rdp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; n = math.hypot(dx, dy) or 1e-9
    best, idx = 0, 0
    for i in range(1, len(pts) - 1):
        x0, y0 = pts[i]; dd = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / n
        if dd > best: best, idx = dd, i
    if best > eps: return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]
def simplify(P, eps):
    far = max(range(len(P)), key=lambda i: math.hypot(P[i][0] - P[0][0], P[i][1] - P[0][1]))
    return rdp(P[:far + 1], eps)[:-1] + rdp(P[far:], eps)
paths, kept = [], []
for r in sorted(out_rings, key=area_km2, reverse=True):
    a = area_km2(r)
    if a < MIN_KM2: continue
    P = [proj(*c) for c in r]
    s = simplify(P, EPS)
    if len(s) < 4: continue
    kept.append((round(a), len(s)))
    paths.append("M" + " ".join(f"{x:.1f},{y:.1f}" for x, y in s[:-1]) + "Z")
d_attr = "".join(paths)
src = '''# -*- coding: utf-8 -*-
"""The island of Ireland as one SVG path, made once from Natural Earth (public
domain, 1:10m admin-0 countries) by _build/make-ireland.py: the
Republic and Northern Ireland dissolved into a single outline, so one path
carries the land and its coast and no border is drawn; islands under %d km2
dropped; simplified to about a kilometre. Equirectangular, scaled by cos
53.5 degrees. project() places any point on the same drawing."""

W, H = %.1f, %.1f
_LAT1, _LON0, _K, _S = %r, %r, %r, %r


def project(lat, lon):
    """(x, y) in the drawing's viewBox for a latitude and longitude."""
    return ((lon - _LON0) * _K * _S, (_LAT1 - lat) * _S)


ISLAND = %r
''' % (MIN_KM2, W, H, LAT1, LON0, K, SC, d_attr)
open(OUT, "w").write(src)
print("rings", len(out_rings), "kept", kept, "path chars", len(d_attr))
