import sys


N = int(sys.stdin.readline())

for _ in range(N):
    W, K = map(int, sys.stdin.readline().split())
    print(W * K // 2)