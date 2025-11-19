import sys


a, b, n, k = map(int, sys.stdin.readline().split())
cnt = 0
flag = False
for i in range(1, a + 1):
    for j in range(1, b + 1):
        cur = 0
        while True:
            cur += 1
            cnt += 1
            if cnt == k:
                print(i, j)
                flag = True
                break
            if cur == n:
                break
        if flag:
            break
    if flag:
        break