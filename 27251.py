import sys


N = int(sys.stdin.readline())
res = 0

for i in range(1, N + 1):
    if i <= 10:
        print("*" * i**2)
    else:
        print("*" * 100, end='')
        print("...")