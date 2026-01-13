import sys

N = int(sys.stdin.readline())

if N * N <= 100000000:
    print("Accepted")
else:
    print("Time limit exceeded")