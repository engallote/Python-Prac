import sys

A, B, C = map(int, sys.stdin.readline().split())

if A + B == C or A + C == B or B + C == A:
    print(1)
elif A * B == C or A * C == B or B * C == A:
    print(2)
else:
    print(3)