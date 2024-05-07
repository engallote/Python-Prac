import sys


N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline().rstrip()

    num, idx = 0, 0
    for i in range(len(s)):
        if s[i] != '!':
            idx = i
            if s[i] == '1':
                num = 1
            break

    if idx + 1 < len(s):
        num = 1

    if idx == 0 or idx % 2 == 0:
        print(num)
    else:
        print(1 - num)
