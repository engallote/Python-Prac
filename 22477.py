import sys


N = int(sys.stdin.readline())
arr = [sys.stdin.readline() for _ in range(N)]

M = int(sys.stdin.readline())
open = False
for _ in range(M):
    s = sys.stdin.readline()
    if s in arr:
        if open:
            open = False
            print("Closed by %s" %s, end='')
        else:
            open = True
            print("Opened by %s" %s, end='')
    else:
        print("Unknown %s" %s, end='')