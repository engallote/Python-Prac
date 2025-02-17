import sys


N, M = map(int, sys.stdin.readline().split())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(N):
    for j in range(M):
        res += (arr1[i] + arr2[j]) * max(arr1[i], arr2[j])


print(res)
