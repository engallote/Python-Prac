import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if N <= 50 and M <= 10:
    print("White")
elif M > 30:
    print("Red")
else:
    print("Yellow")