import sys
import math

N = int(sys.stdin.readline())

div = N / math.pi
div = div ** 0.5

print(2 * math.pi * div)