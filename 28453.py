import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in arr:
    if i < 250:
        print(4, end=' ')
    elif 250 <= i <= 274:
        print(3, end=' ')
    elif 275 <= i < 300:
        print(2, end=' ')
    else:
        print(1, end=' ')
