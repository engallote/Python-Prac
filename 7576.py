import sys
from collections import deque


def bfs():
    chk = set()
    q = deque()
    need = 0

    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                q.append((i, j))
            elif mp[i][j] == 0:
                need += 1

    chk.add((0, 0))
    time, size = 0, 0

    while q:
        size = len(q)
        while size:
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and mp[nx][ny] == 0:
                    mp[nx][ny] = 1
                    need -= 1
                    chk.add((nx, ny))
                    q.append((nx, ny))
            size -= 1
        time += 1

    if need: return -1
    return time - 1


M, N = map(int, sys.stdin.readline().rstrip().split())
mp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

print(bfs())