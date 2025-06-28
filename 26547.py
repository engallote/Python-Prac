import sys


N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    print(s)

    if len(s) == 1:
        continue

    for i in range(1, len(s) - 1):
        print(s[i], end='')
        for _ in range(len(s) - 2):
            print(" ", end='')
        print(s[len(s) - i - 1])

    for i in range(len(s) - 1, -1, -1):
        print(s[i], end='')
    print()