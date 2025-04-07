import sys


N = int(sys.stdin.readline())

for _ in range(N):
    cur = 0
    s = sys.stdin.readline().rstrip()
    for i in s:
        if 'a' <= i <= 'z':
            print(i, end='')
        else:
            if cur == 0:
                print(i.lower(), end='')
            else:
                print("_%c" %i.lower(), end='')
        cur += 1
    print()