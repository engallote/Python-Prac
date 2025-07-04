import sys


sh, sm = map(int, sys.stdin.readline().split(":"))
eh, em = map(int, sys.stdin.readline().split(":"))

h, m = 0, 0
if em >= sm:
    m = em - sm
else:
    m = 60 - sm + em
    sh += 1

h = 24 - sh + eh

print('{0:02d}'.format(h), end=':')
print('{0:02d}'.format(m))