import sys

T = int(sys.stdin.readline())
arr = []

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))

    res = 0
    for i in range(2, 21):
        idx = -1
        for j in range(1, i):
            if arr[j] > arr[i]:
                idx = j
                break

        if idx == -1:
            continue

        num = arr[i]

        for j in range(i, idx, -1):
            arr[j] = arr[j - 1]
            res += 1

        arr[idx] = num

    print(arr[0], res)
