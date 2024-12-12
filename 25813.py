import sys


s = sys.stdin.readline().rstrip()

uid, fid = s.index('U'), s.rindex('F')

for i in range(len(s)):
    if i == uid or i == fid:
        print(s[i], end='')
    elif i < uid or i > fid:
        print("-", end='')
    else:
        print("C", end='')