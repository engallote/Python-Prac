import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

print(sum(arr))

res = 0
for i in range(N):
    if arr2[i] == 0:
        res += arr[i]

print(res)