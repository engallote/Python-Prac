import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = [0, 0, 0, 0]

for i in arr:
    res[i] += 1

if res[1] < N:
    print(1)
    if res[2] != N:
        print(2)
    else:
        print(3)
elif res[2] < N:
    print(2)
    if res[1] != N:
        print(1)
    else:
        print(3)
elif res[3] < N:
    print(3)
    if res[2] != N:
        print(2)
    else:
        print(1)