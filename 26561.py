import sys


N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    for i in range(1, b + 1):
        if i % 7 == 0:
            a -= 1
        if i % 4 == 0:
            a += 1

    print(a)