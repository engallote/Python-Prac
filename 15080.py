import sys

h1, m1, s1 = map(int, sys.stdin.readline().rstrip().split(" : "))
h2, m2, s2 = map(int, sys.stdin.readline().rstrip().split(" : "))

res = 0
if s2 >= s1:
    res += s2 - s1
else:
    res += 60 - s1 + s2
    m1 += 1

if m2 >= m1:
    res += (m2 - m1) * 60
else:
    res += (60 - m1 + m2) * 60
    h1 += 1

if h2 >= h1:
    res += (h2 - h1) * 3600
else:
    res += (24 - h1 + h2) * 3600

print(res)