import sys

s = sys.stdin.readline().rstrip()
idx = 0

while idx < len(s):
    print(s[idx], end='')
    n = ord(s[idx]) - ord('A') + 1
    idx += n
