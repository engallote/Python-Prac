import sys

s = sys.stdin.readline().rstrip()

if s.find('(') > 0:
    idx = s.index('(')
    print(s[:idx])
    print(s[idx + 1 : -1])
else:
    print(s)
    print("-")