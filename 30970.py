import sys


N = int(sys.stdin.readline())
f, s = [], []

for _ in range(N):
    q, p = map(int, sys.stdin.readline().split())
    f.append((q, p))
    s.append((q, p))

f.sort(key=lambda x: (-x[0], x[1]))
s.sort(key=lambda x: (x[1], -x[0]))

print(f[0][0], f[0][1], f[1][0], f[1][1])
print(s[0][0], s[0][1], s[1][0], s[1][1])