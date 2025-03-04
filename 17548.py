import sys


s = sys.stdin.readline().rstrip()
c = s.count('e') * 2
res = "h"

for _ in range(c):
    res += "e"

res += "y"

print(res)