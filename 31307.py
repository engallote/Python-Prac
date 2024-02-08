import sys


N, K = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

tmp, cnt = 0, 0
for i in arr:
    tmp += i
    if tmp > 5 * K:
        break
    cnt += 1

print(cnt)