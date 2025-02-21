import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

e, o = 0, 0
for i in arr:
    if i % 2 == 0:
        e += 1
    else:
        o += 1

for i in range(1, 1000001):
    if e > o and i % 2 == 0 and not i in arr:
        print(i)
        break
    elif e < o and i % 2 != 0 and not i in arr:
        print(i)
        break