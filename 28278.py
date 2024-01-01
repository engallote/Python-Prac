import sys


N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    n = list(map(int, sys.stdin.readline().split()))

    if n[0] == 1:
        arr.append((n[1]))
    elif n[0] == 2:
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(-1)
    elif n[0] == 3:
        print(len(arr))
    elif n[0] == 4:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)