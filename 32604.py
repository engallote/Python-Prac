import sys


N = int(sys.stdin.readline())
ap, bp, flag = 0, 0, True
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if ap > a or bp > b:
        flag = False

    ap = a
    bp = b

if flag:
    print("yes")
else:
    print("no")