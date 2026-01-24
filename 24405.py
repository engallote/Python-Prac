import sys

s = sys.stdin.readline().rstrip()
l, r, el, er = 0, 0, 0, 0

for i in s:
    if i == '|':
        if er == 0:
            l += 1
        else:
            r += 1
    elif i == '(':
        el = 1
    elif i == ')':
        er = 1

if el == 1 and er == 1 and l > 0 and l == r:
    print("correct")
else:
    print("fix")