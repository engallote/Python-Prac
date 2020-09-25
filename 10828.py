import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    tmp = list(sys.stdin.readline().split())
    order = tmp[0]

    if order == "push":
        x = int(tmp[1])
        arr.append(x)
    elif order == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif order == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif order == "size":
        print(len(arr))
    else:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
