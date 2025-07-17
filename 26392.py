import sys


N, r, s = map(int, sys.stdin.readline().split())

for _ in range(N):
    mx, mn = 1000000000, -1
    for i in range(r):
        ss = sys.stdin.readline().rstrip()
        for j in ss:
            if j == '#':
                mx = min(mx, i)
                mn = max(mn, i)

    print(mn - mx)