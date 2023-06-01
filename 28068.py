import sys

N = int(sys.stdin.readline())
p, m = [], []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        m.append((a, b))
    else:
        p.append((a, b))

p.sort(key=lambda x: x[0])
m.sort(key=lambda x: -x[1])

cur = 0

for i in range(len(p)):
    if cur < p[i][0]:
        print(0)
        exit(0)
    cur -= p[i][0]
    cur += p[i][1]

for i in range(len(m)):
    if cur < m[i][0]:
        print(0)
        exit(0)
    cur -= m[i][0]
    cur += m[i][1]

print(1)