import sys


N, M = map(int, sys.stdin.readline().split())
res = [0 for _ in range(M)]
for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))

    for j in range(M):
        res[j] += arr[j]

A = int(sys.stdin.readline())

if M == A:
    print(sum(res))
else:
    mx = 0
    l, r, s, w = 1, A, 0, 0

    for i in range(A):
        s += res[i]

    mx = s

    while l <= r:
        s -= res[l - 1]
        if w == 0:
            s += res[r]

        l += 1
        if r + 1 < M:
            r += 1
        else:
            w = 1
        if mx < s:
            mx = s

    print(mx)