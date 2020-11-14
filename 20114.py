import sys

N, H, W = map(int, sys.stdin.readline().split())
arr = []

for _ in range(H):
    arr.append(list(sys.stdin.readline().rstrip()))

M = N * W
for t in range(0, M, W):
    hs = set()
    for i in range(H):
        for j in range(t, t + W):
            if arr[i][j] != '?':
                hs.add(arr[i][j])

    if len(hs) == 0 or len(hs) > 1:
        print("?", end='')
    else:
        print(hs.pop(), end='')