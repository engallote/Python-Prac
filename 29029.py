import sys


N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
n, w, e, s = 0, 0, 0, 0

for i in arr:
    if i == 'N':
        n += 1
    elif i == 'W':
        w += 1
    elif i == 'E':
        e += 1
    elif i == 'S':
        s += 1

print(N - max(n, w, e, s))