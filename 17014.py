import sys


chk = [False for _ in range(2000000)]
arr = []

for i in range(2, 2000000):
    if chk[i]:
        continue
    arr.append(i)
    for j in range(i + i, 2000000, i):
        chk[j] = True


N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    mul = num * 2

    for i in range(2, mul):
        if not chk[i] and not chk[mul - i]:
            print(i, mul - i)
            break