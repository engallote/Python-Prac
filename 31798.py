import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == 0:
    print(c ** 2 - b)
elif b == 0:
    print(c ** 2 - a)
else:
    print(int((a + b) ** 0.5))