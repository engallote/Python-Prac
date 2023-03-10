import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
zero, another = [], []
arr.sort()

res = 0
for i in range(len(arr)):
    if arr[i] % 10 == 0:
        zero.append(arr[i])
    else:
        another.append(arr[i])

for i in range(len(zero)):
    while zero[i] > 10 and M > 0:
        res += 1
        zero[i] -= 10
        M -= 1
    if zero[i] == 10:
        res += 1

for i in range(len(another)):
    while another[i] > 10 and M > 0:
        res += 1
        another[i] -= 10
        M -= 1

print(res)