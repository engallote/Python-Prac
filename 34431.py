import math
import sys


N = int(sys.stdin.readline()) / 1000
M = int(sys.stdin.readline()) / 60
K = int(sys.stdin.readline())

print(math.ceil(N * M * K / 100))