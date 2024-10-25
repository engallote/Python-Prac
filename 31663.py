import sys


N = int(sys.stdin.readline())
arr = []
mxl = 0
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    mxl = max(mxl, len(s))
    arr.append(s)

for i in range(mxl):
    cnt, res = 0, 0
    for j in range(N):
        if len(arr[j]) <= i:
            continue

        res += ord(arr[j][i])
        cnt += 1

    res = res // cnt
    print(chr(res), end='')