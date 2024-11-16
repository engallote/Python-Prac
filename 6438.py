import sys


N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline().rstrip()

    for i in range(len(s) - 1, -1, -1):
        print(s[i], end='')
    print()