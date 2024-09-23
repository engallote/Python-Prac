import sys


N = sys.stdin.readline().rstrip()
res = []

for i in range(1, int(N) + 1):
    res.append(str(i))
    tmp = ''.join(res)

    if N.count(tmp) == 0 or N.index(tmp) != 0:
        break

    if tmp == N:
        print(i)
        res = []
        break

if len(res) != 0:
    print(-1)