import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    res = (M - N + 1) * (N + M) // 2

    print("Scenario #%d:" % (i + 1))
    print(int(res))
    print()