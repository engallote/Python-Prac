import sys


def east(i, j):
    idx = 0
    for k in range(j, N):
        if arr[i][k] == st[idx]:
            idx += 1
        else:
            break
        if idx == 5:
            break

    if idx >= 5:
        return 1
    else:
        return 0


def west(i, j):
    idx = 0
    for k in range(j, -1, -1):
        if arr[i][k] == st[idx]:
            idx += 1
        else:
            break
        if idx == 5:
            break

    if idx >= 5:
        return 1
    else:
        return 0


def north(i, j):
    idx = 0
    for k in range(i, -1, -1):
        if arr[k][j] == st[idx]:
            idx += 1
        else:
            break
        if idx == 5:
            break

    if idx >= 5:
        return 1
    else:
        return 0


def south(i, j):
    idx = 0
    for k in range(i, N):
        if arr[k][j] == st[idx]:
            idx += 1
        else:
            break
        if idx == 5:
            break

    if idx >= 5:
        return 1
    else:
        return 0


def up(i, j):
    idx, c, tmp = 0, j, 0
    for k in range(i, -1, -1):
        if arr[k][c] == st[idx]:
            idx += 1
        else:
            break
        c -= 1
        if c < 0 or idx >= 5:
            break

    if idx >= 5:
        tmp += 1

    idx, c = 0, j
    for k in range(i, -1, -1):
        if arr[k][c] == st[idx]:
            idx += 1
        else:
            break
        c += 1
        if c == N or idx >= 5:
            break

    if idx >= 5:
        tmp += 1
    return tmp


def down(i, j):
    idx, c, tmp = 0, j, 0
    for k in range(i, N):
        if arr[k][c] == st[idx]:
            idx += 1
        else:
            break
        c -= 1
        if c < 0 or idx >= 5:
            break

    if idx >= 5:
        tmp += 1

    idx, c = 0, j
    for k in range(i, N):
        if arr[k][c] == st[idx]:
            idx += 1
        else:
            break
        c += 1
        if c == N or idx >= 5:
            break

    if idx >= 5:
        tmp += 1
    return tmp


N = int(sys.stdin.readline())
arr, st = [], ['M', 'O', 'B', 'I', 'S']

for _ in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    arr.append(tmp)

res = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'M':
            res += east(i, j)
            res += west(i, j)
            res += north(i, j)
            res += south(i, j)

            res += up(i, j)
            res += down(i, j)

print(res)
