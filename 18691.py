import sys


N = int(sys.stdin.readline())

for _ in range(N):
    G, C, E = map(int, sys.stdin.readline().split())
    E -= C

    if E <= 0:
        print(0)
        continue

    if G == 1:
        print(E)
    elif G == 2:
        print(E * 3)
    else:
        print(E * 5)