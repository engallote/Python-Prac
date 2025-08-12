import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
res, hand = 0, 0

for i in range(len(s)):
    if s[i] == '1':
        res += 1
        hand = 2
    else:
        if hand > 0:
            hand -= 1
            res += 1

print(res)