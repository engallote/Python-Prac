import sys


N, M = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

for _ in range(T):
    num = int(sys.stdin.readline())

    if num <= 1000:
        print(num, num * N)
    else:
        print(num, 1000 * N + (num - 1000) * M)