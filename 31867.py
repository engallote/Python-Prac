import sys

N = sys.stdin.readline()
K = sys.stdin.readline().rstrip()

o, e = 0, 0
for i in K:
    num = int(i)
    if num % 2 == 0:
        e += 1
    else:
        o += 1

if e > o:
    print(0)
elif e < o:
    print(1)
else:
    print(-1)