import sys

a, b, c, m = map(int, sys.stdin.readline().split())

cur, time, work = 0, 0, 0

while time < 24:
    if cur + a <= m:
        cur += a
        work += b
    else:
        cur -= c
        if cur < 0:
            cur = 0
    time += 1

print(work)