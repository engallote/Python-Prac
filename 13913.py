import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
q = deque()
q.append(N)
chk = [100000000000 for _ in range(100001)]
visit = [-1 for _ in range(100001)]
chk[N] = 0

while q:
    x = q.popleft()

    if x == M:
        print(chk[M])
        idx = M
        res = [M]
        while visit[idx] != -1:
            res.append(visit[idx])
            idx = visit[idx]

        print(*res[::-1])
        break

    if x * 2 <= 100000 and chk[x * 2] > chk[x] + 1:
        chk[x * 2] = chk[x] + 1
        visit[x * 2] = x
        q.append(x * 2)
    if x + 1 <= 100000 and chk[x + 1] > chk[x] + 1:
        chk[x + 1] = chk[x] + 1
        visit[x + 1] = x
        q.append(x + 1)
    if x - 1 >= 0 and chk[x - 1] > chk[x] + 1:
        chk[x - 1] = chk[x] + 1
        visit[x - 1] = x
        q.append(x - 1)