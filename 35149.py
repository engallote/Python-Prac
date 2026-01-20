import sys

N, M = map(int, sys.stdin.readline().split())
s, e, w, r, a, v = 0, 0, 0, 0, 0, 0

for _ in range(N):
    arr = list(sys.stdin.readline().rstrip())
    if 'S' in arr:
        s += arr.count('S')
    if 'E' in arr:
        e += arr.count('E')
    if '#' in arr:
        w += arr.count('#')
    if 'U' in arr or 'D' in arr or 'L' in arr or 'R' in arr:
        r += arr.count('U')
        r += arr.count('D')
        r += arr.count('L')
        r += arr.count('R')
    if 'A' in arr:
        a += arr.count('A')
    if 'V' in arr:
        v += arr.count('V')

if s != 1 or e != 1:
    print(-1)
elif a == 0 and v == 0:
    if w <= 1 and r <= 1:
        print(1)
    else:
        print(2)
elif a == 0 and v > 0:
    print(3)
else:
    print(4)