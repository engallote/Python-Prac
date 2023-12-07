import sys

p, r = map(int, sys.stdin.readline().split())

if p / r < 0.2:
    print('weak')
elif 0.2 <= p / r < 0.4:
    print('normal')
elif 0.4 <= p / r < 0.6:
    print('strong')
else:
    print('very strong')