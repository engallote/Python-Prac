import sys


while True:
    N, M = map(int, sys.stdin.readline().rstrip().split())

    if N == 0 and M == 0:
        break

    trr, hrr = [0 for _ in range(101)], [0 for _ in range(101)]
    t, h = 0, 0
    for _ in range(N):
        num = int(sys.stdin.readline())
        trr[num] += 1
        t += num

    for _ in range(M):
        num = int(sys.stdin.readline())
        hrr[num] += 1
        h += num

    flag = False
    for i in range(0, 101):
        if trr[i] == 0:
            continue
        else:
            for j in range(0, 101):
                if hrr[j] > 0:
                    if t - i + j == h - j + i:
                        print(i, j)
                        flag = True
                        break
        if flag:
            break
    if not flag:
        print(-1)
