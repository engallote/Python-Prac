import sys


N = sys.stdin.readline().rstrip()
M = sys.stdin.readline().rstrip()

for i in M:
    if i in N:
        continue
    print(i, end='')