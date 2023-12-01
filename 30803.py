import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
Q = int(sys.stdin.readline())

res = sum(arr)
print(res)
for _ in range(Q):
    arr2 = list(map(int, sys.stdin.readline().split()))

    if arr2[0] == 1:
        if arr[arr2[1] - 1] < 0:
            arr[arr2[1] - 1] = -arr2[2]
        else:
            res -= arr[arr2[1] - 1]
            res += arr2[2]
            arr[arr2[1] - 1] = arr2[2]
    else:
        if arr[arr2[1] - 1] > 0:
            res -= arr[arr2[1] - 1]
        else:
            res += -arr[arr2[1] - 1]
        arr[arr2[1] - 1] *= -1

    print(res)