import sys

N, G = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(N)]

cnt, emp = 0, N
for _ in range(G):
    num = int(sys.stdin.readline())
    cnt += num

    while num > 0:
        if emp == 0:
            for i in range(N):
                if arr[i] == 1:
                    arr[i] = 2
                    num -= 1
                    break
        else:
            for i in range(N):
                if arr[i] == 0:
                    if num >= 2:
                        arr[i] += 2
                        num -= 2
                        emp -= 1
                    else:
                        arr[i] = 1
                        num = 0
                        emp -= 1
                    break

for i in range(N):
    print(arr[i])