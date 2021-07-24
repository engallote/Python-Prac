import sys


N = int(sys.stdin.readline())
res, num = 10000000000000, 0

for i in range(1, N + 1):
    price, arr = map(str, sys.stdin.readline().rstrip().split())
    z, o, t = 0, 0, 0
    for j in arr:
        if j == '0':
            z += 1
        elif j == '1':
            o += 1
        elif j == '2':
            t += 1

    if t >= 2 and o >= 1 and z >= 1:
        if int(price) < res:
            res = int(price)
            num = i

print(num)