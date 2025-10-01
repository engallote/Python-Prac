import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    d = N % 25 + 0.5

    if 17 <= d < 25:
        print("OFFLINE")
    else:
        print("ONLINE")