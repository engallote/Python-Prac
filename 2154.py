import sys


N = int(sys.stdin.readline())
s = ""

for i in range(1, N + 1):
    s += str(i)

print(s.find(str(N)) + 1)