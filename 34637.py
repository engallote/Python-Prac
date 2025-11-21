import sys


n, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num in arr:
        continue
    arr.append(num)

res = len(arr)
if res > k:
    res = k
print(res)