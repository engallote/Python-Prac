import sys

T = int(sys.stdin.readline())

for _ in range(T):
    sys.stdin.readline().rstrip()
    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    arr1, arr2 = list(map(int, sys.stdin.readline().rstrip().split(" "))), list(map(int, sys.stdin.readline().rstrip().split(" ")))
    c, e, res = sum(arr1), sum(arr2), 0
    avg1, avg2 = 0, 0

    avg1 = c / N
    avg2 = e / M

    for i in range(N):
        c -= arr1[i]
        e += arr1[i]

        if c / (N - 1) > avg1 and e / (M + 1) > avg2:
            res += 1
        c += arr1[i]
        e -= arr1[i]
    print(res)