import sys


N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    s = sys.stdin.readline().rstrip()

    if "CD" in s:
        continue
    res += 1

print(res)