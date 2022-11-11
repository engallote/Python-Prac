import sys

c = sys.stdin.readline().rstrip()
line, cur = 'ILOVEYONSEI', c
res = 0

for i in line:
    res += abs(ord(cur) - ord(i))
    cur = i

print(res)