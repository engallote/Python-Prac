import sys


K = int(sys.stdin.readline())
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(N):
    for j in range(M):
        if A[i] + K == B[j]:
            res += 1

print(res)