import sys


P = int(sys.stdin.readline())
C = int(sys.stdin.readline())

res = P * 50 - C * 10
if P > C:
    res += 500

print(res)