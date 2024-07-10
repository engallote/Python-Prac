import sys


N = int(sys.stdin.readline())

for _ in range(N):
    a, b, c = sys.stdin.readline().split()
    i = int(b)
    j = int(c)

    print(a[0:i], end='')
    print(a[j:])