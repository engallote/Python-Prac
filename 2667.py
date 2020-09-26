import sys
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    st = set()
    global cnt

    while q:
        x, y = q.popleft()
        st.add((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and mp[nx][ny] == 1:
                mp[nx][ny] = 0
                q.append((nx, ny))

    return len(st)


N = int(sys.stdin.readline())
mp = [list(map(int, sys.stdin.readline().rstrip())) for x in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
num = 0
arr = []

for i in range(N):
    for j in range(N):
        if mp[i][j] == 1:
            cnt = 0
            num += 1
            arr.append(bfs(i, j))

print(num)
for i in sorted(arr):
    print(i)