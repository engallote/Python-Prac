import sys


arr = [0 for _ in range(10)]
for _ in range(5):
    N = int(sys.stdin.readline())
    arr[N] += 1

for i in range(10):
    if arr[i] % 2 != 0:
        print(i)