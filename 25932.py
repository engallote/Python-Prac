import sys


N = int(sys.stdin.readline())

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))

    print(*arr)
    if 17 in arr and 18 in arr:
        print("both")
    elif 17 in arr:
        print("zack")
    elif 18 in arr:
        print("mack")
    else:
        print("none")
    print()