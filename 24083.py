import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

if (A + B) % 12 == 0:
    print(12)
else:
    print((A + B) % 12)