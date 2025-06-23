import sys


N = int(sys.stdin.readline())
d = {}

for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()
    d[b] = a

s = sys.stdin.readline().rstrip()
for i in range(0, len(s), 4):
    t = s[i:i+4]

    if t in d.keys():
        print(d[t], end='')
    else:
        print("?", end='')