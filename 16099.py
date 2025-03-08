import sys


N = int(sys.stdin.readline())

for _ in range(N):
    lt, wt, le, we = map(int, sys.stdin.readline().split())
    if lt * wt == le * we:
        print("Tie")
    elif lt * wt > le * we:
        print("TelecomParisTech")
    else:
        print("Eurecom")