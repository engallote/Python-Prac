import sys


N = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
arr = []
for i in tmp:
    if i == 0:
        continue
    arr.append(i)
mul = []
arr.sort()

flag = True
while flag:
    pre, idx = arr[0], 0
    flag = False
    for i in range(1, len(arr)):
        if arr[i] == 0:
            continue
        if arr[i] == pre:
            flag = True
            arr[i] *= 2
            arr[idx] = 0

        pre = arr[i]
        idx = i
    arr.sort()

print(arr[-1])