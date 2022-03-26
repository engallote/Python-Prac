import sys

N = int(sys.stdin.readline())
Y, K = 0, 0
for _ in range(N):
    a, b = 0, 0
    for _ in range(9):
        y, k = map(int, sys.stdin.readline().rstrip().split())
        Y += y
        K += k

        if Y > K:
            a += 1
        elif Y < K:
            b += 1

    if a > b:
        print("Yonsei")
    elif a == b:
        print("Draw")
    else:
        print("Korea")