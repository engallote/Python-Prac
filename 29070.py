import sys


a, b, h, w = map(int, sys.stdin.readline().split())
res = h // a

if h % a > 0:
    res += 1

res2 = w // b

if w % b > 0:
    res2 += 1

print(res * res2)