import sys


N, K, T = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(N):
    if T > K:
        T = T + arr[i] - abs(T - K)
    elif T < K:
        T = T + arr[i] + abs(T - K)
    else:
        T += arr[i]
    res += abs(T - K)

print(res)