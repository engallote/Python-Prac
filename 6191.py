import sys


def bfs():
    q = [(0, 0)]
    chk[0][0] = 0

    while True:
        size = len(q)
        while size > 0:
            x, y = q.pop()
            if x == N - 1 and y == M - 1:
                return
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= M or chk[nx][ny] <= chk[x][y] + 1 or arr[nx][ny] == '*':
                    continue

                chk[nx][ny] = chk[x][y] + 1
                path[nx][ny] = (x, y)
                q.append((nx, ny))
            size -= 1
    return


N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
chk = [[100000000] * M for _ in range(N)]
path = [[(-1, -1)] * M for _ in range(N)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

bfs()

res = []
x, y = N - 1, M - 1
while True:
    res.append((x + 1, y + 1))
    nx, ny = path[x][y]
    x = nx
    y = ny

    if x == -1 and y == -1:
        break

res.reverse()
for i in res:
    x, y = i
    print(x, y)