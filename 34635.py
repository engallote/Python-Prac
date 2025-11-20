import sys


r, g, b = map(int, sys.stdin.readline().split())
ro, go, bo = map(int, sys.stdin.readline().split())
rg, gb = map(int, sys.stdin.readline().split())

r -= ro
g -= go
b -= bo

if r < 0:
    r = 0
if g < 0:
    g = 0
if b < 0:
    b = 0
res = 0
if rg >= r:
    res += r
    rg -= r
    r = 0
else:
    print(-1)
    exit(0)
if rg >= g:
    res += g
    rg -= g
    g = 0
else:
    res += rg
    g -= rg
if gb >= g:
    res += g
    gb -= g
    g = 0
else:
    print(-1)
    exit(0)
if gb >= b:
    res += b
    print(res)
else:
    print(-1)
    exit(0)