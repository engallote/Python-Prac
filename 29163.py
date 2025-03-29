import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = 0

for i in arr:
    if i % 2 == 0:
        res += 1

if N - res < res:
    print("Happy")
else:
    print("Sad")