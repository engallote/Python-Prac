import sys

N = int(sys.stdin.readline().rstrip())
s1, s2 = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()
res = 0

for i in range(N):
    if s1[i] != s2[i]:
        res += 1

print(res)