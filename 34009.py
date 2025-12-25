import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

if N % 2 == 0:
    print("Alice")
else:
    print("Bob")