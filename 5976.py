import sys

N = int(sys.stdin.readline().rstrip())
arr = [[0 for _ in range(N)] for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, num, d = 0, 0, 1, 0

while True:
    if arr[x][y] != 0:
        x -= dx[d]
        y -= dy[d]

        d = (d + 1) % 4
        x += dx[d]
        y += dy[d]

        if arr[x][y] != 0:
            break

    arr[x][y] = num
    num += 1
    x += dx[d]
    y += dy[d]
    if x < 0 or y < 0 or x >= N or y >= N:
        x -= dx[d]
        y -= dy[d]

        d = (d + 1) % 4
        x += dx[d]
        y += dy[d]
        if x < 0 or y < 0 or x >= N or y >= N:
            break

for i in range(0, N):
    tmp = list(map(str, arr[i]))
    print(' '.join(tmp))