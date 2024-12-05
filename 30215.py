import sys

O, A, K = map(int, sys.stdin.readline().split())
res = 0

for i in range(1, 100):
    for j in range(1, 100):
        if A * i + K * j == O:
            res = 1
            break

    if res == 1:
        break

print(res)