import sys


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a == b + c or b == a + c or c == a + b:
    print(1)
else:
    print(0)