import sys


N = int(sys.stdin.readline())

mx, idx = 0, 0
for i in range(N):
    m = int(sys.stdin.readline())

    if m > mx:
        mx = m
        idx = i

if idx == 0:
    print("S")
else:
    print("N")