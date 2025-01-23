import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

for i in s:
    if i == 'J':
        print('O', end='')
    elif i == 'O':
        print('I', end='')
    else:
        print('J', end='')