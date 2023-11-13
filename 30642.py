import sys

N = int(sys.stdin.readline())
who = sys.stdin.readline().rstrip()
cur = int(sys.stdin.readline())

if who == 'annyong':
    if cur % 2 == 1:
        print(cur)
    else:
        if cur + 1 <= N:
            print(cur + 1)
        else:
            print(cur - 1)
else:
    if cur % 2 == 0:
        print(cur)
    else:
        if cur + 1 <= N:
            print(cur + 1)
        else:
            print(cur - 1)