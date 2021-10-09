import sys


def find(sz, num):
    sz2 = len(str(num))
    s = []
    for _ in range(sz - sz2):
        s.append('0')
    for i in str(num):
        s.append(i)

    l, r = 0, len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break

    for i in range(len(N) ** 10):
        if find(len(N), int(N) + i):
            print(i)
            break
