import sys
from collections import deque


def bfs(root):
    dist = [10000000000 for _ in range(N + 1)]
    q = deque()
    q.append(root)
    dist[root] = 0
    maxIdx, maxDist = 0, 0

    while len(q):
        x = q.popleft()

        for next, d in mp[x]:
            if dist[next] > dist[x] + d:
                dist[next] = dist[x] + d
                q.append(next)

    for i in range(1, N + 1):
        if maxDist < dist[i]:
            maxIdx = i
            maxDist = dist[i]

    return maxIdx, maxDist


N = int(sys.stdin.readline())
mp = [[] for _ in range(N + 1)]
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    idx = arr[0]

    for i in range(1, len(arr), 2):
        if arr[i] == -1:
            break
        next = arr[i]
        d = arr[i + 1]
        mp[idx].append((next, d))

idx1, dist1 = bfs(1)
idx2, dist2 = bfs(idx1)

print(max(dist1, dist2))