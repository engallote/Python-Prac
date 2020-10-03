import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
q = deque()
q.append(N)
chk = set()
chk.add(N)
time = 0

while q:
    size = len(q)
    while size:
        x = q.popleft()

        if x == M:
            print(time)

        if x + 1 <= M and x + 1 not in chk:
            chk.add(x + 1)
            q.append(x + 1)
        if x - 1 >= 0 and x - 1 not in chk:
            chk.add(x - 1)
            q.append(x - 1)
        if x * 2 <= 100000 and x * 2 not in chk:
            chk.add(x * 2)
            q.append(x * 2)
        size -= 1
    time += 1