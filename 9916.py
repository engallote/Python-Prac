import sys


N = int(sys.stdin.readline())
mul = 1
for i in range(2, N + 1):
    mul *= i

print(str(mul).count('0'))