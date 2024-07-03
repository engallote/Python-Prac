import sys


N = int(sys.stdin.readline())

ans = ""
for _ in range(N):
    s = sys.stdin.readline().rstrip()

    if len(s) > 10:
        continue

    num, big, small, h = 0, 0, 0, 0
    for i in s:
        if 'a' <= i <= 'z':
            small += 1
        elif 'A' <= i <= 'Z':
            big += 1
        elif i == '-':
            h += 1
        else:
            num += 1

    if (big == 0 and small == 0 and h == 0) or big > small:
        continue

    ans = s

print(ans)