import sys


h1, d1, t1 = map(int, sys.stdin.readline().split())
h2, d2, t2 = map(int, sys.stdin.readline().split())

for i in range(100000000):
    if i % t1 == 0:
        h2 -= d1
    if i % t2 == 0:
        h1 -= d2

    if h1 <= 0 and h2 <= 0:
        print("draw")
        break
    elif h1 <= 0:
        print("player two")
        break
    elif h2 <= 0:
        print("player one")
        break