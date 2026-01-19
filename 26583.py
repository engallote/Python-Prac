import sys

while True:
    s = sys.stdin.readline().rstrip()

    if s == "":
        break

    arr = list(map(int, s.split()))

    for i in range(len(arr)):
        res = arr[i]
        if i - 1 >= 0:
            res *= arr[i - 1]
        if i + 1 < len(arr):
            res *= arr[i + 1]

        print(res, end=' ')
    print()