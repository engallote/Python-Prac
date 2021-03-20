import sys

tc = 1
while True:
    Z, I, M, L = map(int, sys.stdin.readline().rstrip().split())

    if Z == 0 and I == 0 and M == 0 and L == 0:
        break

    arr = set()

    while True:
        nxt = (Z * L + I) % M
        if nxt in arr:
            break
        arr.add(nxt)
        L = nxt

    print("Case %d: %d" %(tc, len(arr)))
    tc += 1