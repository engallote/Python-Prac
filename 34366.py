import sys


N = int(sys.stdin.readline())
mx, mn, sx, sn = 0, 10000000000, 0, 100000000000
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))

    for i in range(1, arr[0] + 1):
        if arr[i] > mx:
            mx = arr[i]
        if sum(arr[1:]) > sx:
            sx = sum(arr[1:])
        if arr[i] < mn:
            mn = arr[i]
        if sum(arr[1:]) < sn:
            sn = sum(arr[1:])

print(mx)
print(mn)
print(sx)
print(sn)