import sys


A, B, K = map(int, sys.stdin.readline().rstrip().split())

if A == B and B == K:
    print(1)
elif A < K or B < K:
    print(0)
else:
    a = A // K
    b = B // K

    print(a * b - max(0, A // K - 2) * max(0, B // K - 2))