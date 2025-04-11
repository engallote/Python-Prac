import sys


A, B, C = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

if T <= 30:
    print(A)
else:
    T -= 30
    res = A
    res += T // B * C
    if T % B != 0:
        res += C

    print(res)