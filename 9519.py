import math
import sys

N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
l = len(s)
hs = []
cnt = 0

while N > 0:
    tmp = []
    arr = []

    for i in range(0, l, 2):
        arr.append(s[i])
        if i + 1 < l:
            tmp.append(s[i + 1])
    tmp.reverse()

    for i in range(len(tmp)):
        arr.append(tmp[i])

    s = ''.join(arr)
    if s in hs:
        idx = N % cnt - 1
        s = hs[idx]
        break

    hs.append(s)
    N -= 1
    cnt += 1

print(s)