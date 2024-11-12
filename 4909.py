import sys


while True:
    arr = list(map(int, sys.stdin.readline().split()))

    if sum(arr) == 0:
        break

    arr.sort()
    res = sum(arr[1:5])

    if res % 4 == 0:
        print(res // 4)
    else:
        print(res / 4)