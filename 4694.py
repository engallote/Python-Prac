import sys


def find(idx):
    global end
    if end:
        return
    if idx == len(puz):
        for i in range(4):
            for j in range(4):
                if mp[i][j] == 0:
                    return

        end = True
        for i in range(4):
            res = list(map(str, mp[i]))
            print(''.join(res))
        return

    for i in range(4):
        for j in range(4):
            tmp = puz[idx]
            r, c = len(tmp), len(tmp[0])
            # print(i, j, r, c)
            if i + r > 4 or j + c > 4:
                continue

            flag = True
            for a in range(i, i + r):
                for b in range(j, j + c):
                    if mp[a][b] != 0 and tmp[a - i][b - j] == 1:
                        flag = False
                        break
            if flag:
                for a in range(i, i + r):
                    for b in range(j, j + c):
                        if tmp[a - i][b - j] == 1:
                            mp[a][b] = idx + 1

                find(idx + 1)

                for a in range(i, i + r):
                    for b in range(j, j + c):
                        if tmp[a - i][b - j] == 1:
                            mp[a][b] = 0


while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    end = False
    mp = [[0] * 4 for _ in range(4)]
    puz = []
    for t in range(0, N):
        R, C = map(int, sys.stdin.readline().split())
        arr = [[int(x) for x in sys.stdin.readline().rstrip()] for _ in range(R)]
        puz.append(arr)

    find(0)
    if end:
        print()
    else:
        print("No solution possible")
        print()
