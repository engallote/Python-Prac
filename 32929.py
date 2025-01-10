import sys


N = int(sys.stdin.readline()) - 1

if N == 0 or N % 3 == 0:
    print("U")
elif N % 3 == 1:
    print("O")
else:
    print("S")