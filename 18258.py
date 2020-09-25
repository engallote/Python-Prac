import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque()

for _ in range(N):
    tmp = list(sys.stdin.readline().split())
    order = tmp[0]

    if order == "push":
        x = int(tmp[1])
        arr.append(x)
    elif order == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif order == "back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif order == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif order == "size":
        print(len(arr))
    else:
        if len(arr) == 0:
            print(1)
        else:
            print(0)