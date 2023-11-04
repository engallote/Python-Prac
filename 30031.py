import sys

N = int(sys.stdin.readline())

res = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if a == 136 or b == 136:
        res += 1000
    elif a == 142 or b == 142:
        res += 5000
    elif a == 148 or b == 148:
        res += 10000
    else:
        res += 50000

print(res)