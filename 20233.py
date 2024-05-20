import sys
import math

a = int(sys.stdin.readline())
x = int(sys.stdin.readline())
b = int(sys.stdin.readline())
y = int(sys.stdin.readline())
T = int(sys.stdin.readline())

A, B = a, b

if T > 30:
    A += (T - 30) * x * 21

if T > 45:
    B += (T - 45) * y * 21

print(A, B)