import sys


while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    arr = [sys.stdin.readline().rstrip() for _ in range(N)]
    sum = [0 for _ in range(N)]
    max, res = -1, 0

    for i in range(N):
        for j in range(i + 1, N):
            if len(arr[i]) != len(arr[j]):
                continue

            flag = True
            for k in range(len(arr[i])):
                if arr[i].count(arr[i][k]) == arr[j].count(arr[i][k]) and arr[j].count(arr[j][k]) == arr[i].count(arr[i][k]):
                    continue
                flag = False
                break

            if flag:
                sum[i] += 1
        if max < sum[i]:
            max = sum[i]
            res = i

    print(arr[res], max)