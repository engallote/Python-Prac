import sys


t1, m1, t2, m2 = map(int, sys.stdin.readline().split())

time = 0
while True:
    if t1 == t2 and m1 == m2:
        break

    m1 += 1
    time += 1
    if m1 == 60:
        m1 = 0
        t1 += 1

    if t1 == 24:
        t1 = 0

print(time, time // 30)