import sys


N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
time = list(map(int, sys.stdin.readline().split()))

res = x[-1]
for i in range(N - 1, -1, -1):
    if i < N - 1:
        res += x[i + 1] - x[i]

    if time[i] > res:
        res += time[i] - res

print(res + x[0])