import sys

while True:
    s = sys.stdin.readline().rstrip()

    if s == '#':
        break

    arr = s.split()
    for i in arr:
        if len(i) <= 3:
            print(i, end=' ')
        else:
            arr = i[1:-1]
            print(i[0], end='')
            print(''.join(reversed(arr)), end='')
            print(i[-1], end=' ')

    print()