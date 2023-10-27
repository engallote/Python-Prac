import sys

N = int(sys.stdin.readline())

res = 0
for i in range(N):
    s = sys.stdin.readline().rstrip()

    if "01" in s or "OI" in s:
        res += 1

print(res)