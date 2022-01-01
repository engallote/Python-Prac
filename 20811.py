import sys


N = int(sys.stdin.readline())
arr = [0 for _ in range(N)]
arr[1] = arr[2] = 1

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    res = 2
    for i in range(3, N):
        arr[i] = arr[i - 1] + arr[i - 2]
        res += arr[i]
        if res >= N:
            print(i)
            break