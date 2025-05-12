import sys


N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
cur, res = 1, 0

for i in S:
    if i == 'L':
        if cur - 1 >= 1:
            cur -= 1
    else:
        if cur + 1 <= 3:
            cur += 1

    if cur == 3:
        res += 1

print(res)