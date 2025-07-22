import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
pre, miss, empty = arr[0], 0, 0

for i in arr:
    if pre == i:
        continue
    elif pre < i:
        miss += i - pre
    else:
        empty += pre - i

    pre = i

print(empty, miss)