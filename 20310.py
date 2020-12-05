import sys

arr = list(sys.stdin.readline().rstrip())
zero, one, size = 0, 0, len(arr)

for i in arr:
    if i == '0':
        zero += 1
    else:
        one += 1

zero //= 2
one //= 2

for i in range(size - 1, 0, -1):
    if arr[i] == '0' and zero > 0:
        zero -= 1
        arr[i] = '3'

for i in range(size):
    if arr[i] == '1' and one > 0:
        one -= 1
        arr[i] = '3'

for i in arr:
    if i != '3':
        print(i, end='')