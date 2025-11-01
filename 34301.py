import sys


N = int(sys.stdin.readline())
a, b, c, d, e = 0, 0, 0, 0, 0

e = N // 150
N %= 150

d = N // 30
N %= 30

c = N // 15
N %= 15

b = N // 5
N %= 5

a = N

print(a, b, c, d, e)