import sys

N = int(sys.stdin.readline())
res = 0

for i in range(1, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            res += 1

print(res)