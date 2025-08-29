import sys


N = int(sys.stdin.readline())

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(2, arr[0] + 1):
        if arr[i - 1] < arr[i]:
            continue
        else:
            if i + 1 <= arr[0] and arr[i - 1] < arr[i + 1]:
                print(i)
            else:
                print(i - 1)
            break