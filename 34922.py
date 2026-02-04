import sys
import math

a, b = map(float, sys.stdin.readline().split())
r = float(sys.stdin.readline())

rm = r ** 2 * math.pi / 4

print(a * b - rm)
