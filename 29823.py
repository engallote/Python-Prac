import sys


N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())

n, s, w, e = 0, 0, 0, 0
for i in arr:
    if i == 'N':
        n += 1
    elif i == 'S':
        s += 1
    elif i == 'W':
        w += 1
    else:
        e += 1

print(abs(n - s) + abs(e - w))