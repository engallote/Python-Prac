import sys


N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
arr = [0] * 10

for i in S:
    if i == 'L':
        for j in range(10):
            if arr[j] == 0:
                arr[j] = 1
                break
    elif i == 'R':
        for j in range(9, -1, -1):
            if arr[j] == 0:
                arr[j] = 1
                break
    else:
        arr[int(i)] = 0

print(*arr, sep='')