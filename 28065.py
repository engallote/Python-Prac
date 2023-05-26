import sys

N = int(sys.stdin.readline())
l, r, who = 1, N, 1

for _ in range(N):
    if who == 0:
        print(l, end=' ')
        l += 1
    else:
        print(r, end=' ')
        r -= 1
    who = 1 - who