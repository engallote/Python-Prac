import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

for i in range(N):
    if i + 1 < N and s[i + 1] == 'J':
        print(s[i])