import sys


N = int(sys.stdin.readline())
W, V = map(int, sys.stdin.readline().split())

a = W / V

if a >= N:
    print(1)
else:
    print(0)