import sys

s = sys.stdin.readline().rstrip()
res = 1
for i in range(1, len(s)):
    if s[i - 1] < s[i]:
        continue
    else:
        res += 1

print(res)