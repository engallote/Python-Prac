import sys


T = int(sys.stdin.readline())
f = 1

for _ in range(T):
    N = int(sys.stdin.readline())

    if 48 <= N:
        continue
    else:
        f = 0
        break

if f == 1:
    print("True")
else:
    print("False")