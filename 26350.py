import sys


N = int(sys.stdin.readline())

for n in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    tmp = sorted(arr[1:])
    flag = True

    print("Denominations:", *arr[1:])
    for i in range(1, arr[0]):
        if tmp[i - 1] * 2 <= tmp[i]:
            continue
        else:
            flag = False
    if flag:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")

    print()