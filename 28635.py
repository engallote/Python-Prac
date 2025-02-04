import sys


M = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
res = 0

while True:
    if a == b:
        break

    a += 1
    if a > M:
        a = 1
    res += 1

print(res)