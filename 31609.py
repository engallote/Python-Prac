import sys


N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

s.sort()

print(s[0])
for i in range(1, N):
    if s[i] == s[i - 1]:
        continue
    print(s[i])