import sys


s = sys.stdin.readline()
h, m = map(int, sys.stdin.readline().split(":"))
hours = h * 60 + m

day = sys.stdin.readline().rstrip()
i = int(sys.stdin.readline())
fr = int(sys.stdin.readline())
holi = int(sys.stdin.readline())

if day == "sat" or day == "sun":
    hours *= 2
if i == 1:
    hours *= 2
if fr == 1:
    hours *= 3
if holi == 1:
    hours *= 3

print(hours // 60, end=':')
print('{0:02d}'.format(hours % 60))