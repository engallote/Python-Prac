import sys


A = int(sys.stdin.readline())

if A == 0:
    print(0)
elif A == 1:
    print(1)
else:
    res, cnt = 1, 1
    while res < A:
        res *= 2
        cnt += 1

    print(cnt)