import sys

N = int(sys.stdin.readline())
arr = set(sys.stdin.readline().split())

M = int(sys.stdin.readline())

for i in sys.stdin.readline().split():
    if i in arr:
        print(1)
    else:
        print(0)