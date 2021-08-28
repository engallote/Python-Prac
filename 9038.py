import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    st = sys.stdin.readline().split()
    cur, res = 0, 1

    for i in range(0, len(st)):
        if cur + len(st[i]) <= N:
            cur += len(st[i])
        else:
            cur = len(st[i])
            res += 1

        if cur + 1 <= N:
            cur += 1
        else:
            if i == len(st) - 1:
                break
            cur = 0
            res += 1

    print(res)