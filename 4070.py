import sys

t = 0
while True:
    t += 1
    N, K = map(int, sys.stdin.readline().split())
    if N == 0 and K == 0:
        break

    arr = []
    for _ in range(N):
        name = sys.stdin.readline().rstrip()
        arr.append(len(name))

    if N < K:
        print("Case %d: no" %t)
        continue
    arr = sorted(arr)

    div, leng = 0, 0
    flag = True
    for i in range(0, N, K):
        leng = 0
        for j in range(i, i + K):
            leng += arr[j]

        div = leng / K
        for j in range(i, i + K):
            if abs(arr[j] - div) > 2:
                flag = False
                break
            if not flag:
                break

    if flag:
        print("Case %d: yes\n" %t)
    else:
        print("Case %d: no\n" % t)