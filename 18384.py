import sys

T = int(sys.stdin.readline().rstrip())
chk = [False for _ in range(1100000)]
prime = []
chk[0], chk[1] = True, True

for i in range(1100000):
    if chk[i]:
        continue
    prime.append(i)
    for j in range(i + i, 1100000, i):
        chk[j] = True

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    res = 0
    for i in arr:
        for j in prime:
            if i <= j:
                res += j
                break
    print(res)