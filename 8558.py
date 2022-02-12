import sys

N = int(sys.stdin.readline())

if N <= 1:
    print(1)
else:
    res = 1
    for i in range(2, N + 1):
        res *= i

    print(str(res)[-1])
