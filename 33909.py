import sys


s, c, o, n = map(int, sys.stdin.readline().split())
res = 0

while True:
    if s == 0:
        if n >= 2:
            s += 2
            n -= 2
    elif s == 1:
        if n >= 1:
            s += 1
            n -= 1

    if c < 2:
        if o >= 2:
            o -= 2
            c += 4
    elif c < 4:
        if o >= 1:
            o -= 1
            c += 2

    if o == 0:
        if c >= 2:
            c -= 2
            o = 1

    if n == 0:
        if s >= 1:
            s -= 1
            n = 1

    if s >= 2 and c >= 4 and o >= 1 and n >= 1:
        s -= 2
        c -= 4
        o -= 1
        n -= 1
        res += 1
    else:
        break

print(res)