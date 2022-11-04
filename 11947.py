import sys

T = int(sys.stdin.readline().rstrip())

for t in range(T):
    N = int(sys.stdin.readline().rstrip())
    size = 10 ** len(str(N))
    half = size // 2
    res, num = 0, 0

    if half <= N:
        for i in str(half):
            num += 9 - int(i)
            num *= 10
        num //= 10
        print(num * half)
    else:
        for i in str(N):
            num += 9 - int(i)
            num *= 10
        num //= 10
        print(num * N)
