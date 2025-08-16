import sys


N = int(sys.stdin.readline())
mn, mx, idx1, idx2 = 100000000000, -1, -1, -1

for i in range(N):
    num = int(sys.stdin.readline())

    if mn > num:
        mn = num
        idx1 = i

    if mx < num:
        mx = num
        idx2 = i

if idx1 == 0:
    print("ez")
elif idx2 == 0:
    print("hard")
else:
    print("?")