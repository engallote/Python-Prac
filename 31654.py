import sys


A, B, C = map(int, sys.stdin.readline().split())
if A + B == C:
    print("correct!")
else:
    print("wrong!")