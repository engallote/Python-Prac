import sys


S = int(sys.stdin.readline())
M = int(sys.stdin.readline())
L = int(sys.stdin.readline())

res = S + 2 * M + 3 * L

if res >= 10:
    print("happy")
else:
    print("sad")