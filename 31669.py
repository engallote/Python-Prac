import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

for i in range(M):
    flag = 1
    for j in range(N):
        if arr[j][i] == 'O':
            flag = 0
            break

    if flag == 1:
        print(i + 1)
        flag = 2
        break

if flag != 2:
    print("ESCAPE FAILED")