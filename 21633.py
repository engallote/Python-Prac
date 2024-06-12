import sys


N = int(sys.stdin.readline())

res = N / 100 + 25

if res > 2000:
    res = 2000
elif res < 100:
    res = 100

print("{:.2f}".format(res))