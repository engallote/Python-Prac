import sys


N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    s, p = sys.stdin.readline().split()

    idx = s.find('x')

    if idx == -1:
        idx = s.find('X')

    print(p[idx].upper(), end='')