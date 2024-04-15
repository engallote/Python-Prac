import sys


N = int(sys.stdin.readline())

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    mp = [[0 for _ in range(arr[0])] for _ in range(arr[0])]

    idx = 2
    for _ in range(arr[1]):
        x, y = arr[idx], arr[idx + 1]
        mp[x][y] = 1
        mp[y][x] = 1

        idx += 2

    q = [0]
    hs = set()
    while len(q) > 0:
        size = len(q)
        for _ in range(size):
            x = q.pop()
            hs.add(x)

            for i in range(arr[0]):
                if mp[x][i] == 1:
                    mp[x][i] = mp[i][x] = -1
                    q.append(i)

    if len(hs) == arr[0]:
        print("Connected.")
    else:
        print("Not connected.")