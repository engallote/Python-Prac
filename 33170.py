import sys


A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

if A + B + C <= 21:
    print(1)
else:
    print(0)