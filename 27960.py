import sys


A, B = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(10)]

for i in range(9, 0, -1):
    if A & (1 << i) != 0:
        A -= (1 << i)
        arr[i] += 1
    if B & (1 << i) != 0:
        B -= (1 << i)
        arr[i] += 1

if A == 1:
    arr[0] += 1
if B == 1:
    arr[0] += 1

C = 0
for i in range(0, 10):
    if arr[i] == 1:
        C += (1 << i)

print(C)