import sys


N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline().rstrip()

    if 6 <= len(s) <= 9:
        print("yes")
    else:
        print("no")