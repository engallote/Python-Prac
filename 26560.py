import sys


N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline().rstrip()

    if s[-1] == '.':
        print(s)
    else:
        s += "."
        print(s)