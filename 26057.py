import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

d = M

while True:
    if N - d < d:
        break
    d += 1

print(d - (N - d))