import sys


D = int(sys.stdin.readline())
E = int(sys.stdin.readline())

for _ in range(E):
    c = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())

    if c == '+':
        D += N
    else:
        D -= N

print(D)