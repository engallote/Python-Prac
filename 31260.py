import sys

m, c = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())

all = m * 100 + c
dd = all // 4

for i in range(dd + 200):
    if (i + (i + d)) * 2 == all:
        print((i + d) // 100, (i + d) % 100)
        print(i // 100, i % 100)
        break