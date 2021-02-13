import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    dic = dict()
    score = [[0 for _ in range(3)] for _ in range(N*2)]
    idx = 0

    for _ in range(N):
        arr = list(sys.stdin.readline().rstrip().split())
        a, b = 0, 0

        if int(arr[1]) > int(arr[3]):
            a = 3
        elif int(arr[1]) == int(arr[3]):
            a, b = 1, 1
        else:
            b = 3

        if arr[0] in dic:
            score[dic[arr[0]]][0] += a
            score[dic[arr[0]]][1] += int(arr[1]) - int(arr[3])
        else:
            dic[arr[0]] = idx
            score[idx][0] = a
            score[idx][1] = int(arr[1]) - int(arr[3])
            score[idx][2] = arr[0]
            idx += 1

        if arr[4] in dic:
            score[dic[arr[4]]][0] += b
            score[dic[arr[4]]][1] += int(arr[3]) - int(arr[1])
        else:
            dic[arr[4]] = idx
            score[idx][0] = b
            score[idx][1] = int(arr[3]) - int(arr[1])
            score[idx][2] = arr[4]
            idx += 1

    score.sort(key=lambda x:(-x[0], -x[1]))

    for i in range(idx):
        print(score[i][0], score[i][2])

    print()