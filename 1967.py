import sys

sys.setrecursionlimit(100000)


def dfs(idx):
    if len(mp[idx]) == 0: return 0
    global res
    max1, max2 = 0, 0

    for next, cost in mp[idx]:
        tmp = dfs(next) + cost
        if tmp > max1:
            if tmp > max2:
                max1 = max2
                max2 = tmp
            else:
                max1 = tmp

    res = max(max1 + max2, res)

    return max2


N = int(sys.stdin.readline())
mp = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    mp[a].append((b, c))
res = 0
dfs(1)
print(res)