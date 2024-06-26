import sys

N = int(sys.stdin.readline())
arr, res = [], 0
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

M = int(sys.stdin.readline())
for _ in range(M):
    num = int(sys.stdin.readline()) - 1
    res += arr[num]

print(res)