import sys


T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())

    m, res = 1, 0
    for j in range(1, N + 1):
        m *= j
        res = m % 10

    print(res)