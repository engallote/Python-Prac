import sys

a, b = map(int, sys.stdin.readline().split())

res = ''
if a == b:
    res = '='
elif a == 0:
    if b == 5:
        res = '<'
    else:
        res = '>'
elif a == 2:
    if b == 0:
        res = '<'
    else:
        res = '>'
elif a == 5:
    if b == 2:
        res = '<'
    else:
        res = '>'
else:
    if b == 0 or b == 2 or b == 5:
        res = '<'
    else:
        res = '='

print(res)