import sys


N = int(sys.stdin.readline())

if N <= 100000 and N % 2024 == 0:
    print("Yes")
else:
    print("No")