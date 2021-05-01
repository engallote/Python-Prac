import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

res = str(A * B * C)
arr = [0 for _ in range(10)]

for i in res:
    arr[int(i)] += 1

for i in range(10):
    print(arr[i])