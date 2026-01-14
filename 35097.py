import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    res = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            res += i * j

    print(res)