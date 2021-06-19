import sys

while True:
    arr = sys.stdin.readline().rstrip().split()

    if arr[0] == '0':
        break

    idx, cnt = 1, 0
    for i in range(1, len(arr)):
        num = int(arr[i])

        if 1 <= num - cnt:
            for j in range(0, num - cnt):
                print(idx, end=' ')

        idx += 1
        cnt = num

    print()