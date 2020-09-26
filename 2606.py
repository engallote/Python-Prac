import sys
from collections import deque


def bfs(root):
    chk = [root]
    q = deque()
    q.append(root)

    while q:
        idx = q.popleft()

        for next in arr[idx]:
            if next not in chk:
                chk.append(next)
                q.append(next)

    return len(chk) - 1


N = int(sys.stdin.readline())
M = int(input())
arr = {}

for i in range(1, N + 1):
    arr[i] = set()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].add(b)
    arr[b].add(a)

print(bfs(1))