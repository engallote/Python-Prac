import sys


N = int(sys.stdin.readline())

for i in range(N):
    arr = list(map(int, sys.stdin.readline().rstrip()))
    a = arr[0] * 10 + arr[1]
    b = arr[2] * 10 + arr[3]
    res = (a ** 2) + (b ** 2) - 1

    if res % 7 == 0:
        print("YES")
    else:
        print("NO")