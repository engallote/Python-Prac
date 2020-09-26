import sys
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    st = set()

    while q:
        x, y = q.popleft()
        st.add((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and mp[nx][ny] == 1:
                mp[nx][ny] = 0
                q.append((nx, ny))

    return len(st)


T = int(sys.stdin.readline())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    mp = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        mp[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                mp[i][j] = 0
                cnt += 1
                bfs(i, j)

    print(cnt)