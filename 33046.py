import sys


A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

cur = 1
A += B - 1

while A > 0:
    cur += 1

    if cur == 5:
        cur = 1
    A -= 1

C += D - 1
while C > 0:
    cur += 1

    if cur == 5:
        cur = 1

    C -= 1

print(cur)