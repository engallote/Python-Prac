import sys


N, M = map(int, sys.stdin.readline().split())
name = {}

for _ in range(N):
    s, f = sys.stdin.readline().rstrip().split()
    key = s[0] + f[0]
    if key in name:
        name[key] = "ambiguous"
    else:
        name[key] = s + " " + f

for _ in range(M):
    s = sys.stdin.readline().rstrip()

    if s in name:
        print(name[s])
    else:
        print("nobody")