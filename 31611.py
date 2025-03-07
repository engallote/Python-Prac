import sys


X = int(sys.stdin.readline())

if X < 10:
    if X == 2 or X == 9:
        print(1)
    else:
        print(0)
else:
    if (X - 2) % 7 == 0:
        print(1)
    else:
        print(0)