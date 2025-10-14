import sys


N = int(sys.stdin.readline())

for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()

    for i in b:
        print((int(i) + int(a)) % 10, end='')

    print()
