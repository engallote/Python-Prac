import sys

s = sys.stdin.readline().rstrip()

res = 0
for i in range(len(s)):
    if s[i] == 'k':
        if i + 3 < len(s):
            if s[i + 1] == 'i' and s[i + 2] == 'c' and s[i + 3] == 'k':
                res += 1

print(res)