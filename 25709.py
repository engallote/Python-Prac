import sys


arr = list(sys.stdin.readline().rstrip())

cnt = 0
while True:
    if len(arr) == 0 or arr.count('0') == len(arr):
        break

    if '1' in arr:
        for i in range(len(arr)):
            if arr[i] == '1':
                arr.pop(i)
                break

        if len(arr) != 0:
            num = int(''.join(arr))
            arr = list(str(num))
    else:
        num = int(''.join(arr)) - 1
        arr = list(str(num))

    cnt += 1

print(cnt)