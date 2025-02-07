import sys


N, a, b = map(int, sys.stdin.readline().split())
fb, f, bb = 0, 0, 0

for i in range(1, N + 1):
    if i % a == 0 and i % b == 0:
        fb += 1
    elif i % a == 0 and i % b != 0:
        f += 1
    elif i % a != 0 and i % b == 0:
        bb += 1

print(f, bb, fb)