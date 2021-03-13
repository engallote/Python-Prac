import sys

N = int(sys.stdin.readline().rstrip())

while True:
    N += 1
    num = N
    arr = [0 for _ in range(10)]
    flag = True

    while num > 0:
        arr[num % 10] += 1
        if arr[num % 10] >= 2:
            flag = False
            break
        num //= 10

    if flag:
        print(N)
        break