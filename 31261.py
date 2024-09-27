import sys


a, b = map(int, sys.stdin.readline().split())

for _ in range(2):
    b += a
    b *= a

print(b)