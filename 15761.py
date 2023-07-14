import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

res = 0
for i in arr:
    if i >= res:
        res += 1
    else:
        break

print(res)