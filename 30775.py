import sys


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

mod = sum(arr) % N

if mod != 0:
    mod = 1

print(sum(arr) // N + mod)