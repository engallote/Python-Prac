import sys

K = int(sys.stdin.readline())

for i in range(1, K + 1):
    N = int(sys.stdin.readline())
    m = sys.stdin.readline().rstrip()
    arr = []

    for j in m:
        if j in arr:
            continue
        arr.append(j)

    res = 0

    for _ in range(N):
        s = sys.stdin.readline().rstrip()
        for j in arr:
            if s.count(j) > 0:
                res += 1
                break

    print("Data Set %d:" %i)
    print(res)
    print()