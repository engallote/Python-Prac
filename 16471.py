import sys

N = int(sys.stdin.readline())
ju = list(map(int, sys.stdin.readline().split()))
sa = list(map(int, sys.stdin.readline().split()))

ju.sort()
sa.sort()

idx1, idx2, cnt = N - 1, N - 1, 0
while idx2 >= 0:
    while idx1 - 1 >= 0 and ju[idx1] >= sa[idx2]:
        idx1 -= 1

    if ju[idx1] < sa[idx2]:
        cnt += 1

    idx2 -= 1
    if idx1 - 1 >= 0:
        idx1 -= 1
    else:
        break

if cnt >= (N + 1) // 2:
    print("YES")
else:
    print("NO")