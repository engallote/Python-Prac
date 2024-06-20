import sys

N, M = map(int, sys.stdin.readline().split())
arr1, arr2 = list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))
arr2.sort()

res = sum(arr1)

for i in arr2:
    if i == 0:
        continue
    res *= i

print(res)