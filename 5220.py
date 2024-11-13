import sys


N = int(sys.stdin.readline())

for _ in range(N):
    num, b = map(int, sys.stdin.readline().split())

    s = str(bin(num))
    n = s.count("1")

    if n % 2 == 0:
        if b == 1:
            print("Corrupt")
        else:
            print("Valid")
    else:
        if b == 0:
            print("Corrupt")
        else:
            print("Valid")