import sys

N = int(sys.stdin.readline())
arr = set(sys.stdin.readline().rstrip() for _ in range(N))

M = int(sys.stdin.readline())
res = 0
for _ in range(0, M):
    num = sys.stdin.readline().rstrip()

    if num in arr:
        res += 1

print(res)