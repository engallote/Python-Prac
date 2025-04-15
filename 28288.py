import sys


N = int(sys.stdin.readline())
arr = [0, 0, 0, 0, 0]
res, mx = [], 0

for _ in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    for i in range(5):
        if tmp[i] == 'Y':
            arr[i] += 1
            if arr[i] > mx:
                mx = arr[i]

for i in range(5):
    if arr[i] == mx:
        res.append(i + 1)

print(*res, sep=',')