import sys


N, M = map(int, sys.stdin.readline().split())
INF = 1000000000
mp = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    mp[i][i] = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    mp[a][b] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if mp[i][k] + mp[k][j] < mp[i][j]:
                mp[i][j] = mp[i][k] + mp[k][j]

res = INF
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if i != j:
            res = min(res, mp[i][j] + mp[j][i])

print(res if res < INF else -1)