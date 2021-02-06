import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

res = 1
for i in range(2, N + 1):
    num = i
    for j in range(2, K + 1):
        while True:
            if num % j != 0:
                break
            num //= j

    if num <= K:
        res += 1

print(res)