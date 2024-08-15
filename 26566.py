import math
import sys


N = int(sys.stdin.readline())

for _ in range(N):
    a1, b1 = map(int, sys.stdin.readline().split())
    a2, b2 = map(int, sys.stdin.readline().split())

    a2 = a2 ** 2 * math.pi

    if a1 / b1 > a2 / b2:
        print("Slice of pizza")
    else:
        print("Whole pizza")