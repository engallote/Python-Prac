import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

res = 0
for i in arr:
    if i % T == 0:
        res += i // T
    else:
        res += i // T + 1

print(res)
print((N // P), (N % P))