import sys


N = int(sys.stdin.readline())

d, p = 0, 0
for _ in range(N):
    s = sys.stdin.readline().rstrip()

    if s == 'D':
        d += 1
    else:
        p += 1

    if abs(d - p) >= 2:
        break

print("%d:%d" %(d, p))