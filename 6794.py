import sys

N = int(sys.stdin.readline())

if N == 1 or N == 9 or N == 10:
    print(1)
elif 4 <= N <= 6:
    print(3)
else:
    print(2)