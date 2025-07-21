import sys


N = int(sys.stdin.readline())

z, o = 0, 0

for _ in range(N):
    n = int(sys.stdin.readline())

    if n == 0:
        z += 1
    else:
        o += 1

if z > o:
    print(o)
else:
    print(z)