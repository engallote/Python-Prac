import sys


N = int(sys.stdin.readline())

for _ in range(N):
    arr = list(sys.stdin.readline().split())
    res = [0 for _ in range(170)]

    mx = -1
    for i in arr:
        idx = ord(i[0])
        res[idx] += 1
        if mx < res[idx]:
            mx = res[idx]

    print(mx)