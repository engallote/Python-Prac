import sys


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

res = 0
for i in arr:
    res += i - 1

if M > res:
    print("OUT")
else:
    print("DIMI")