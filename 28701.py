import sys

N = int(sys.stdin.readline())

print(int((N + 1) * N / 2))
print(int((N + 1) * N / 2) ** 2)

res = 0
for i in range(1, N + 1):
    res += i ** 3

print(res)