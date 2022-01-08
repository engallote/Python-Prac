import sys


N = int(sys.stdin.readline())

res = 100000000000000
a, b, c = 0, 0, 0
for i in range(1, N + 1):
    if N % i != 0:
        continue
    for j in range(i, N + 1):
        if (N // i) % j != 0:
            continue
        k = (N // i) // j

        num = i * j * 2 + ((i + j) * 2 * k)
        if res > num:
            res = num
            a, b, c = i, j, k


print(a, b, c)