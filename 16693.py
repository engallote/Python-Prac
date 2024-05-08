import sys
import math

a1, p1 = map(int, sys.stdin.readline().split())
a2, p2 = map(int, sys.stdin.readline().split())

tmp = a2 ** 2 * math.pi

if a1 / p1 > tmp / p2:
    print("Slice of pizza")
else:
    print("Whole pizza")