import sys

N = int(sys.stdin.readline())
num = int(sys.stdin.readline())
map = [[0 for _ in range(N)] for _ in range(N)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
x, y, number, d = 0, 0, N * N, 0
nx, ny = 0, 0
while True:
    # print(x, y)
    map[x][y] = number

    if number == num:
        nx = x
        ny = y

    number -= 1

    if number == 0:
        break

    while 0 > x + dir[d][0] or x + dir[d][0] >= N or 0 > y + dir[d][1] or y + dir[d][1] >= N or map[x + dir[d][0]][y + dir[d][1]] != 0:
        # print(" >> ", d, ":: ", x + dir[d][0], y + dir[d][1])
        d += 1
        d %= 4

    x += dir[d][0]
    y += dir[d][1]

for i in range(N):
    for j in range(N):
        print(map[i][j], end=' ')
    print()

print(nx + 1, ny + 1)