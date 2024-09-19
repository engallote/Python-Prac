import sys


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    res = 0.0
    for _ in range(N):
        x, p, c = sys.stdin.readline().split()
        res += int(p) * float(c)

    print("$%.2f" %res)