import sys


arr = list(map(int, sys.stdin.readline().split()))
m = sum(arr) // 3

res = 0
for i in range(3):
    while arr[i] != m:
        if arr[i] < m:
            if i + 1 < 3 and arr[i + 1] > m:
                arr[i + 1] -= 1
                arr[i] += 1
                res += 1
            elif i - 1 >= 0 and arr[i - 1] > m:
                arr[i - 1] -= 1
                arr[i] += 1
                res += 1
            elif i + 2 < 3 and arr[i + 2] > m:
                arr[i + 2] -= 1
                arr[i] += 1
                res += 2
            elif i - 2 >= 0 and arr[i - 2] > m:
                arr[i - 2] -= 1
                arr[i] += 1
                res += 2
        elif arr[i] > m:
            if i + 1 < 3 and arr[i + 1] < m:
                arr[i + 1] += 1
                arr[i] -= 1
                res += 1
            elif i - 1 >= 0 and arr[i - 1] < m:
                arr[i - 1] += 1
                arr[i] -= 1
                res += 1
            elif i + 2 < 3 and arr[i + 2] < m:
                arr[i + 2] += 1
                arr[i] -= 1
                res += 2
            elif i - 2 >= 0 and arr[i - 2] < m:
                arr[i - 2] += 1
                arr[i] -= 1
                res += 2

print(res)