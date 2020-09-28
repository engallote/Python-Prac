import sys
from collections import deque

def bfs():
    chk = set()
    q = deque()
    q.append((0, 0))
    chk.add((0, 0))
    time, size = 0, 0

    while q:
        size = len(q)
        while size:
            x, y = q.popleft()

            if x == N - 1 and y == M - 1:
                return time

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and mp[nx][ny] == 1:
                    mp[nx][ny] = 0
                    chk.add((nx, ny))
                    q.append((nx, ny))
            size -= 1
        time += 1

N, M = map(int, sys.stdin.readline().rstrip().split())
mp = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

print(bfs() + 1)