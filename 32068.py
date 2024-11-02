import sys


T = int(sys.stdin.readline())

for _ in range(T):
    L, R, S = map(int, sys.stdin.readline().split())
    if S == L or S == R:
        print(1)
        continue
    print(min((S - L) * 2 + 1, (R - S) * 2))