import sys


N = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
res = 0

for i in range(1, N + 1):
    if i % A == 0 and i % B != 0:
        res += 1
    elif i % A != 0 and i % B == 0:
        res += 1

print(res)