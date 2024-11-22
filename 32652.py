import sys


N = int(sys.stdin.readline())
s = "AKARAKA"

for _ in range(1, N):
    s += "RAKA"

print(s)