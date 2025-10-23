import sys


s = sys.stdin.readline().rstrip()
time, w = map(str, s.split(" "))
h, m = map(int, time.split(":"))

if w == "PM" and h < 12:
    h += 12
elif w == "AM" and h == 12:
    h = 0

N = int(sys.stdin.readline())

while N > 0:
    m -= 1
    if m < 0:
        m = 59
        h -= 1

        if h < 0:
            h = 23
    N -= 1

if h == 0:
    h = 12
    w = "AM"
elif h < 12:
    w = "AM"
else:
    if h > 12:
        h -= 12
    w = "PM"
print(h, end=':')
print('{0:02d}'.format(m), end=' ')
print(w)