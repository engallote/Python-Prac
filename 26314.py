import sys


N = int(sys.stdin.readline())

for _ in range(N):
    res = 0
    s = sys.stdin.readline().rstrip()

    tmp = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    print(s)
    if tmp > len(s) / 2:
        print(1)
    else:
        print(0)