import sys


N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    s = sys.stdin.readline()
    if s[0] == 'C':
        res += 1

print(res)