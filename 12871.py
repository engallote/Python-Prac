import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

num = len(s) * len(t)
idx = 0

for i in range(num - len(s)):
    s += s[idx]
    idx += 1

idx = 0
for i in range(num - len(t)):
    t += t[idx]
    idx += 1

if s == t:
    print(1)
else:
    print(0)