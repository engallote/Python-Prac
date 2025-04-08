import sys


N = int(sys.stdin.readline())
h, m, s = 0, 0, 0
for _ in range(N):
    M, S = sys.stdin.readline().rstrip().split(":")

    s += int(S)
    m += int(M)

m += s // 60
s %= 60

h += m // 60
m %= 60

print(f"{h:02d}:{m:02d}:{s:02d}")