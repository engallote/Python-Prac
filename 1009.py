import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    res = a
    b = b % 4 + 4

    for _ in range(2, b + 1):
        res = (res * a) % 10

    if res == 0:
        print(10)
    else:
        print(res)