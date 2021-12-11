import sys


N = int(sys.stdin.readline())
k = int(sys.stdin.readline())
mod = 0
if k % 2 != 0:
    mod = 1
k //= 2

print(N // 2 + k + mod)
print(N // 2 - k)