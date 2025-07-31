import sys


P, Q = map(int, sys.stdin.readline().split())
arr1, arr2 = [], []

for i in range(1, P + 1):
    if P % i == 0:
        arr1.append(i)

for i in range(1, Q + 1):
    if Q % i == 0:
        arr2.append(i)

for i in arr1:
    for j in arr2:
        print(i, j)