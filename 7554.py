import sys


T = int(sys.stdin.readline())

for t in range(1, T + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    res = 0

    for i in range(1, arr[0]):
        for j in range(1, arr[0]):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                res += 1

    print("Scenario #%d:" %t)
    print(res)
    print()
