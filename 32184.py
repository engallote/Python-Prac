import sys


A, B = map(int, sys.stdin.readline().rstrip().split())

res = 0
if A % 2 == 0:
    A -= 1

for _ in range(A, B + 1, 2):
    res += 1

print(res)