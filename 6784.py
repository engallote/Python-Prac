import sys


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

res = 0
for i in range(N):
    ans = sys.stdin.readline().rstrip()
    if arr[i] == ans:
        res += 1

print(res)