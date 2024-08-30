import sys


N = int(sys.stdin.readline())
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

res = 0
for i in range(N):
    if s1[i] == s2[i]:
        continue
    res += 1

print(res)