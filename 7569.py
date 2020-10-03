import sys
from collections import deque


def bfs(cnt, q):
    time = 0
    while q:
        size = len(q)
        while size:
            h, x, y = q.popleft()

            for i in range(6):
                nx, ny, nh = x + dx[i], y + dy[i], h + dh[i]
                if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H and mp[nh][nx][ny] == '0':
                    mp[nh][nx][ny] = 1
                    cnt -= 1
                    q.append((nh, nx, ny))
            size -= 1
        time += 1

    if cnt: return -1
    return time - 1


M, N, H = map(int, sys.stdin.readline().rstrip().split())
mp = [[] for _ in range(H)]
dx, dy, dh = [1, 0, -1, 0, 0, 0], [0, 1, 0, -1, 0, 0], [0, 0, 0, 0, 1, -1]
q = deque()

cnt = 0
for i in range(H):
    for j in range(N):
        mp[i].append(sys.stdin.readline().split())
        for k in range(M):
            if mp[i][j][k] == '1':
                q.append((i, j, k))
            elif mp[i][j][k] == '0':
                cnt += 1

print(bfs(cnt, q))