import sys

T = int(sys.stdin.readline())

for _ in range(T):
    tmp = list(map(int, sys.stdin.readline().split()))
    N = tmp[0]
    arr = tmp[1:]
    arr.sort()
    arr2 = [0 for _ in range(N)]
    arr2[0] = arr[0]

    for i in range(1, N):
        arr2[i] = arr2[i - 1] + arr[i]

    res = 0

    for i in range(2, N + 1):
        l, r, t = 0, i - 1, sys.maxsize
        while r < N:
            mul = arr[r] * i
            if l > 0:
                t = min(t, mul - (arr2[r] - arr2[l - 1]))
            else:
                t = min(t, mul - (arr2[r]))
            l += 1
            r += 1
        res += t

    print(res)