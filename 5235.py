import sys

T = int(sys.stdin.readline())

for _ in range(T):
    lst = list(map(int, sys.stdin.readline().split()))
    e, o = 0, 0
    for i in range(1, len(lst)):
        if lst[i] % 2 == 0:
            e += lst[i]
        else:
            o += lst[i]

    if e > o:
        print("EVEN")
    elif e < o:
        print("ODD")
    else:
        print("TIE")