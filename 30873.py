import sys


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    p, c = map(int, sys.stdin.readline().split())
    arr.append((p, c))

res = 0
for i in range(N):
    p, c = arr[i][0], arr[i][1]

    if abs(p - res) <= c:
        res += 1

print(res)