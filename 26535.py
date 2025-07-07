import sys


N = int(sys.stdin.readline())
n = 0

for i in range(N + 10):
    if i * i >= N:
        n = i + 2
        break

for i in range(n):
    if i == 0 or i == n - 1:
        print('x'*n)
    else:
        print('x', end='')
        print('.'*(n-2), end='')
        print('x')