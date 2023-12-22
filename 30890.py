import sys

X, Y = map(int, sys.stdin.readline().split())
XY = X * Y

for i in range(1, XY + 1):
    if i % X == 0 and i % Y == 0:
        print(3, end='')
    elif i % X == 0:
        print(2, end='')
    elif i % Y == 0:
        print(1, end='')