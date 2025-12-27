import sys


N = int(sys.stdin.readline())

while N >= 10:
    s = str(N)
    tmp = 0
    for i in s:
        tmp += int(i)

    N = tmp

print(N)