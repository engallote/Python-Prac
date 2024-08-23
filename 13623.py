import sys


A, B, C = map(int, sys.stdin.readline().split())

if A == B == C:
    print("*")
elif A != B and B == C:
    print("A")
elif A != B and A == C:
    print("B")
elif A != C and A == B:
    print("C")
