import sys

N, K, a, b = map(int, sys.stdin.readline().split())

print((K - 1) * b + (N - 1) * b, a * (N - 1))