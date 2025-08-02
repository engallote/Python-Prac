import sys


N = int(sys.stdin.readline())

for _ in range(N):
    a, b = sys.stdin.readline().replace(",", " ").split()

    aa = int(a[::-1])
    bb = int(b[::-1])
    cc = str(aa + bb)

    if cc == "0":
        print(0)
    else:
        print(cc[::-1].strip("0"))