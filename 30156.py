import sys


N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    a, b = 0, 0

    for i in s:
        if i == "a":
            a += 1
        else:
            b += 1

    print(min(a, b))