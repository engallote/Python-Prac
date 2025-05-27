import sys


N = int(sys.stdin.readline())

mx, dff = 0, 100000000
for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    if a + b + c < 512:
        continue

    if abs(512 - (a + b + c)) < dff:
        dff = abs(512 - (a + b + c))
        mx = a + b + c

if mx >= 512:
    print(mx)
else:
    print(-1)