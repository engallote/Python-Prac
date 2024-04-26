import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    l, r = 1, 50
    while True:
        mid = (l + r) // 2
        print(mid, end=' ')

        if mid > N:
            r = mid - 1
        elif mid == N:
            print()
            break
        else:
            l = mid + 1