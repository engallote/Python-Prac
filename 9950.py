import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 0 and b == 0 and c == 0:
        break

    if a == 0:
        a = c // b
    elif b == 0:
        b = c // a
    else:
        c = a * b

    print(a, b, c)