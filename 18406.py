import sys

s = sys.stdin.readline().rstrip()
ln = len(s)

l, r = 0, 0

for i in range(ln // 2):
    l += int(s[i])

for i in range(ln // 2, ln):
    r += int(s[i])

if l == r:
    print("LUCKY")
else:
    print("READY")