import sys

N = int(sys.stdin.readline())

for i in range(1, N):
    if N % i == 0:
        a, b = i, N // i

        if a * 2 == b or a == b * 2:
            print(max(a, b) * 4)
            break