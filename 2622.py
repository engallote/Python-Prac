import sys


N = int(sys.stdin.readline())
res = 0

for i in range(1, N):
    for j in range(i, N):
        if N - (i + j) <= 0:
            break
        a, b, c = i, j, N - (i + j)

        if b > c:
            break

        if max(a, b, c) == a:
            if a < b + c:
                res += 1
        elif max(a, b, c) == b:
            if b < a + c:
                res += 1
        else:
            if c < a + b:
                res += 1

print(res)