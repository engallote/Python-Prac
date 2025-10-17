import sys


a, b, x, y = map(int, sys.stdin.readline().split())
aa = (a + x) * 2 + max(b, y) * 2
bb = max(a, x) * 2 + (b + y) * 2
print(min(aa, bb))