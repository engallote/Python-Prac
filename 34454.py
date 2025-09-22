import sys


N = int(sys.stdin.readline())
C = int(sys.stdin.readline())
P = int(sys.stdin.readline())

if P * C >= N:
    print("yes")
else:
    print("no")