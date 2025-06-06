import sys


N = sys.stdin.readline().rstrip()
res, s = 0, "SciComLove"

for i in range(len(N)):
    if N[i] != s[i]:
        res += 1

print(res)