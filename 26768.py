import sys


s = sys.stdin.readline()

for i in s:
    if i == 'a':
        print(4, end='')
    elif i == 'e':
        print(3, end='')
    elif i == 'i':
        print(1, end='')
    elif i == 'o':
        print(0, end='')
    elif i == 's':
        print(5, end='')
    else:
        print(i, end='')