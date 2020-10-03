import sys
from queue import PriorityQueue

N, M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
mp = [dict() for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if b in mp[a]:
        mp[a][b] = min(mp[a][b], c)
    else:
        mp[a][b] = c

INF = sys.maxsize
dist = [INF for _ in range(N + 1)]
dist[K] = 0
q = PriorityQueue()
q.put((0, K))

while q.qsize():
    curCost, x = q.get()

    for next, cost in mp[x].items():
        if dist[next] > curCost + cost:
            dist[next] = curCost + cost
            q.put((dist[next], next))

for i in dist[1:]:
    print(i if i < INF else 'INF')