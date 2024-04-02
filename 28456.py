import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

Q = int(sys.stdin.readline())

for _ in range(Q):
    order = list(map(int, sys.stdin.readline().split()))
    num = order[0]

    if num == 1:
        row = order[1] - 1
        tmp = arr[row][-1]

        for i in range(N - 1, 0, -1):
            arr[row][i] = arr[row][i - 1]
        arr[row][0] = tmp
    else:
        arr2 = []

        for j in range(N):
            tmp = []
            for i in range(N - 1, -1, -1):
                tmp.append(arr[i][j])
            arr2.append(tmp)

        for i in range(N):
            for j in range(N):
                arr[i][j] = arr2[i][j]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()