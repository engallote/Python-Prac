import sys


N, M = map(int, sys.stdin.readline().split())
z, o = 0, 0

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    for i in s:
        if i == "0":
            z += 1
        else:
            o += 1

if z > o:
    print(o)
else:
    print(z)