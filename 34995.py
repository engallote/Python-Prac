import sys

N, M = sys.stdin.readline().rstrip().split()
cost = int(sys.stdin.readline())
M = M.replace("?", "9")
cp = int(M)

if cp >= cost:
    print(cp)
else:
    print(-1)