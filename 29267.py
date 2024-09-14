import sys


N, M = map(int, sys.stdin.readline().split())
k, kp = 0, 0
for _ in range(N):
    s = sys.stdin.readline().rstrip()

    if s == "ammo":
        k += M
    elif s == "save":
        kp = k
    elif s == "load":
        k = kp
    else:
        k -= 1

    print(k)