import sys


d1, m1, y1, n = map(int, sys.stdin.readline().split())
d2, m2, y2 = map(int, sys.stdin.readline().split())

while True:
    if y1 == y2 and m1 == m2 and d1 == d2:
        break

    d1 += 1
    n += 1
    if n == 8:
        n = 1

    if d1 > 30:
        d1 = 1
        m1 += 1

    if m1 > 12:
        m1 = 1
        y1 += 1

print(n)