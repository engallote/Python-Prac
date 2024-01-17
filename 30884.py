import sys

s = sys.stdin.readline().rstrip()
res = []
for i in range(len(s) - 1):
    if s[i] == '(' and s[i + 1] == ')':
        res.append(s[i])
        res.append('1')
    elif s[i] == ')' and s[i + 1] == '(':
        res.append(s[i])
        res.append('+')
    else:
        res.append(s[i])

res.append(')')
print(''.join(res))
