import sys


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

div = K // N

if N == 1:
    print(K)
elif (div + 1) * N + (N - 1) <= K:
    print(div + 1)
elif div * N + (N - 1) <= K:
    print(div)
else:
    print(div - 1)