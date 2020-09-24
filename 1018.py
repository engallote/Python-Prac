N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(input()))

res = 100000000

# W 먼저
for l in range(len(board)):
    if l + 7 >= len(board):
        break
    for k in range(0, M):
        if k + 7 >= M:
            break
        start = -1
        cnt = 0
        for i in range(l, l + 8):
            num = start
            for j in range(k, k + 8):
                if (board[i][j] == 'B' and num == -1) or (board[i][j] == 'W' and num == 1):
                    cnt += 1
                num *= -1
            start *= -1
        res = min(res, cnt)

# B 먼저
for l in range(len(board)):
    if l + 7 >= len(board):
        break
    for k in range(0, M):
        if k + 7 >= M:
            break
        start = 1
        cnt = 0
        for i in range(l, l + 8):
            num = start
            for j in range(k, k + 8):
                if (board[i][j] == 'B' and num == -1) or (board[i][j] == 'W' and num == 1):
                    cnt += 1
                num *= -1
            start *= -1
        res = min(res, cnt)

print(res)