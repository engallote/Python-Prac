import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
res = 0

for i in range(0, len(s), N // 10):
    tmp = 0
    for j in range(i, i + N // 10):
        if s[j] == 'N':
            tmp = 0
            break
        tmp = 1

    res += tmp

print(res)