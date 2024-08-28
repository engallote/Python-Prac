import sys


P = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

res = 0
for i in s:
    if i == 'j' or i == 'i':
        res += 2
    else:
        res += 1

print(res)