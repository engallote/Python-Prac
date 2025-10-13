import sys


X, Y, Z = map(int, sys.stdin.readline().split())
U, V, W = map(int, sys.stdin.readline().split())

print(X * (U // 100) + Y * (V // 50) + Z * (W // 20))