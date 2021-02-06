import sys

N, M = map(int, sys.stdin.readline().split())
map = []

for _ in range(N):
    map.append(list(sys.stdin.readline().rstrip()))

for j in range(0, M):
    for i in range(N - 1, -1, -1):
        print(map[i][j], end='')
    print()