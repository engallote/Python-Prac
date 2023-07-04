import sys


d = 0
for _ in range(10):
    t = int(sys.stdin.readline())

    if t == 1:
        d += 1
        d %= 4
    elif t == 2:
        d += 2
        d %= 4
    else:
        d -= 1
        if d < 0:
            d = 3

if d == 0:
    print('N')
elif d == 1:
    print('E')
elif d == 2:
    print('S')
else:
    print('W')