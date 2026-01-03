import sys

A, B, C, D = map(int, sys.stdin.readline().split())

if max(A + B, C) <= D:
    print("~.~")
elif min(A + B, C) > D:
    print("T.T")
else:
    if A + B < C:
        print("Shuttle")
    else:
        print("Walk")