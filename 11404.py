import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
mp = [[1000000000 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    mp[i][i] = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    mp[a][b] = min(mp[a][b], c)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if mp[i][k] + mp[k][j] < mp[i][j]:
                mp[i][j] = mp[i][k] + mp[k][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(mp[i][j] if mp[i][j] < 1000000000 else 0, end=' ')
    print()