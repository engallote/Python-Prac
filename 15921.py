import sys


N = int(sys.stdin.readline())

if N == 0:
    print("divide by zero")
else:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    avg = sum(arr) / N

    chk = set()
    div = 0
    for i in arr:
        if i in chk:
            continue
        chk.add(i)
        div += i * (arr.count(i) / N)

    if div == 0:
        print("divide by zero")
    else:
        print(format(avg / div, ".2f"))