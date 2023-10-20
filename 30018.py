import sys

N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(N):
    if arr1[i] < arr2[i]:
        res += arr2[i] - arr1[i]

print(res)