import sys


Q = int(sys.stdin.readline())

res = 0
for _ in range(Q):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if x == 1:
        res += y
    else:
        if res < y:
            res = -1
            break
        res -= y

if res == -1:
    print("Adios")
else:
    print("See you next month")