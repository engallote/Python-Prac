import sys


h, m = map(int, sys.stdin.readline().rstrip().split(":"))

time = 120
while True:
    if 7 <= h < 10:
        m += 10
        time -= 5
        if m >= 60:
            m %= 60
            h += 1
    elif 15 <= h < 19:
        m += 10
        time -= 5
        if m >= 60:
            m %= 60
            h += 1
    else:
        if time >= 10:
            m += 10
            time -= 10
        else:
            m += time
            time = 0
        if m >= 60:
            m %= 60
            h += 1

    if time <= 0:
        break
h %= 24

print('{0:02d}'.format(h), end=':')
print('{0:02d}'.format(m))