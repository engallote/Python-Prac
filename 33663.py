import sys


hl, hh = map(int, sys.stdin.readline().split())
sl, sh = map(int, sys.stdin.readline().split())
vl, vh = map(int, sys.stdin.readline().split())
r, g, b = map(int, sys.stdin.readline().split())
M, m = max(r, g, b), min(r, g, b)

V = M
S = 255 * (V - m) / V
H = 0

if r == M:
    H = (60 * (g - b)) / (r - m)
elif g == M:
    H = 120 + (60 * (b - r)) / (g - m)
else:
    H = 240 + (60 * (r - g)) / (b - m)

if H < 0:
    H += 360

if hl <= H <= hh and sl <= S <= sh and vl <= V <= vh:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")