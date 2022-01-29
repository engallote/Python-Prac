import sys


T = int(sys.stdin.readline())
while True:
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    K = int(sys.stdin.readline())

    arr1, arr2, arr3 = [], [], []
    for _ in range(N):
        arr1.append(sys.stdin.readline().rstrip())
    for _ in range(M):
        arr2.append(sys.stdin.readline().rstrip())
    for _ in range(K):
        arr3.append(sys.stdin.readline().rstrip())

    res = []
    for i in arr1:
        for j in arr2:
            for k in arr3:
                res.append("%s %s %s." % (i, j, k))

    for i in res:
        print(i)
    T -= 1
    if T == 0:
        break
    print()