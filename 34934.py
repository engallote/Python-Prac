import sys


N = int(sys.stdin.readline())
ans, year = "", 0

for _ in range(N):
    a, b = sys.stdin.readline().split()
    if int(b) > year:
        year = int(b)
        ans = a

print(ans)