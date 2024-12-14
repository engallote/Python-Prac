import sys


N = int(sys.stdin.readline())
M = float(sys.stdin.readline())

res = N - (N * M / 100)

print("%.6f" %((N - res) / res * 100))