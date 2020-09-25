import sys
from collections import deque


def dfs(idx, chk):
    chk.append(idx)
    for next in range(len(graph[idx])):
        if graph[idx][next] and next not in chk:
            chk = dfs(next, chk)
    return chk


def bfs(root):
    chk = [root]
    q = deque()
    q.append(root)

    while q:
        num = q.popleft()
        for next in range(len(graph[num])):
            if graph[num][next] and next not in chk:
                chk.append(next)
                q.append(next)

    return ' '.join(str(x) for x in chk)


N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * 1001 for _ in range(1001)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b], graph[b][a] = 1, 1

arr = dfs(V, [])
print(' '.join(str(x) for x in arr))
print(bfs(V))