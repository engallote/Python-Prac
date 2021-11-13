import sys


a, b, c = map(int, sys.stdin.readline().split())

mx = max(a, b, c)

two, thr = False, False
if a == b == c:
    thr = True
if mx == a and mx*mx == b*b + c*c:
    two = True
if mx == b and mx*mx == a*a + c*c:
    two = True
if mx == c and mx*mx == a*a + b*b:
    two = True

if two and not thr:
    print(1)
elif thr:
    print(2)
else:
    print(0)