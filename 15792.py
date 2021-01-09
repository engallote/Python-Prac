import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

if N == M:
    print(1)
else:
    print(int(N / M), end='.')

    num = N % M
    for _ in range(1000):
        num *= 10
        print(int(num / M), end='')
        num %= M
