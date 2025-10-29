import sys


n, s = sys.stdin.readline().rstrip().split()
N, cnt = int(n), 1

for i in range(N):
    num = cnt
    ch = ord(s[i])
    num %= 26

    while num > 0:
        num -= 1
        ch += 1
        if ch > 90:
            ch = 65

    print(chr(ch), end='')
    cnt *= 2