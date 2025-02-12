import sys


N = int(sys.stdin.readline())

for _ in range(N):
    d, f, p = map(float, sys.stdin.readline().split())
    print("$%.2f" %(f * p * d))