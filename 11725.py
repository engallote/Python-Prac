import sys
from collections import deque

N = int(sys.stdin.readline())
par = [0 for _ in range(N + 1)]
mp = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    mp[a].append(b)
    mp[b].append(a)

q = deque()
q.append(1)
par[1] = 1

while len(q):
    x = q.popleft()

    for i in mp[x]:
        if par[i] == 0:
            par[i] = x
            q.append(i)

for i in par[2:]:
    print(i)