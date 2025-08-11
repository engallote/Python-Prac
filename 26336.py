import sys


N = int(sys.stdin.readline())

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    cnt = 0

    print(a, b, c)

    for i in range(1, a):
        if i % b == 0 or i % c == 0:
            cnt += 1

    print(cnt)