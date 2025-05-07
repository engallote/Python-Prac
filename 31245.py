import sys


a, b, c= map(int, sys.stdin.readline().split())

print(a, end='')

if a % 10 == b // 10:
    print('\'%d' %(b%10), end='')
else:
    print(b, end='')

if b % 10 == c // 10:
    print('\'%d' % (c % 10), end='')
else:
    print(c, end='')