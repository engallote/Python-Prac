import sys
from collections import deque


def bfs():
    chk = set()
    q = deque()
    q.append((0, 0, 1))
    chk.add((0, 0, 1))
    time = 1

    while q:
        size = len(q)
        while size:
            x, y, k = q.popleft()

            if x == N - 1 and y == M - 1:
                return time

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if mp[nx][ny] == '1' and k == 1 and (nx, ny, 0) not in chk:
                    chk.add((nx, ny, 0))
                    q.append((nx, ny, 0))
                elif mp[nx][ny] == '0' and (nx, ny, k) not in chk:
                    chk.add((nx, ny, k))
                    q.append((nx, ny, k))
            size -= 1
        time += 1

    return -1


N, M = map(int, sys.stdin.readline().split())
mp = []
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(N):
    mp.append(list(sys.stdin.readline().rstrip()))

print(bfs())