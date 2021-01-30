import sys


A, B = map(float, sys.stdin.readline().rstrip().split())
ab, ba = B/A, A/B

T = int(sys.stdin.readline())

for _ in range(T):
    num, type = sys.stdin.readline().split()

    if type == 'A':
        print(float(num) * ab)
    else:
        print(float(num) * ba)