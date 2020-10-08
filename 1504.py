import sys
from queue import PriorityQueue


def solve(s, e):
    dist = [INF for _ in range(N + 1)]
    dist[s] = 0

    q = PriorityQueue()
    q.put((s, 0))

    while q.qsize():
        x, cost = q.get()

        if x == e or dist[x] < cost:
            continue

        for next, nextCost in mp[x].items():
            if dist[next] > nextCost + cost:
                dist[next] = nextCost + cost
                q.put((next, dist[next]))

    return dist[e]


N, M = map(int, sys.stdin.readline().split())
mp = [dict() for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a in mp[b]:
        mp[b][a] = mp[a][b] = min(mp[a][b], c)
    else:
        mp[a][b] = mp[b][a] = c

a, b = map(int, sys.stdin.readline().split())

INF = 1000000000
bet = solve(a, b)
if bet == INF:
    print(-1)
else:
    res = min(solve(1, a) + solve(b, N), solve(1, b) + solve(a, N)) + bet
    print(res if res < INF else -1)