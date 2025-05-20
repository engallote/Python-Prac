import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

print(N)
print(M)

ms = str(M)

for i in range(len(ms) - 1, -1, -1):
    print(int(ms[i]) * N)

print(N * M)