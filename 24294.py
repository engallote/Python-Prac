import sys


w1 = int(sys.stdin.readline())
h1 = int(sys.stdin.readline())
w2 = int(sys.stdin.readline())
h2 = int(sys.stdin.readline())

if w1 < w2:
    print((w1 + 2) * h1 + (w2 + 2) * (h2 + 2) - (w1 * h1) - (w2 * h2))
else:
    print((w2 + 2) * h2 + (w1 + 2) * (h1 + 2) - (w1 * h1) - (w2 * h2))