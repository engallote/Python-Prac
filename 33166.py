import sys


P, Q = map(int, sys.stdin.readline().split())
A, B = map(int, sys.stdin.readline().split())

if Q <= P:
    print(A * Q)
else:
    res = P * A
    Q -= P
    print(res + Q * B)