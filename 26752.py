import sys


h, m, s = map(int, sys.stdin.readline().split())

s += 1
if s == 60:
    s = 0
    m += 1
if m == 60:
    m = 0
    h += 1
if h == 24:
    h = 0

print("{0:02d}".format(h),end=':')
print("{0:02d}".format(m),end=':')
print("{0:02d}".format(s))