import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

cnt, num = 0, 0
for i in range(1, N):
    loc = i - 1
    item = arr[i]

    while 0 <= loc and item < arr[loc]:
        arr[loc + 1] = arr[loc]
        loc -= 1
        if arr == arr2:
            num = 1
            break

    if loc + 1 != i:
        arr[loc + 1] = item
        if arr == arr2:
            num = 1
            break
    if num == 1:
        break

print(num)