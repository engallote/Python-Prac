import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

p, m, s, cnt = 1, 1, 0, 0
for i in range(1, N):
    if arr[i] > arr[i - 1]:
        if s == -1:
            m = max(m, cnt)
            cnt = 2
        elif s == 1:
            cnt += 1
        else:
            cnt = 2
        s = 1
    elif arr[i] < arr[i - 1]:
        if s == -1:
            cnt += 1
        elif s == 1:
            p = max(p, cnt)
            cnt = 2
        else:
            cnt = 2
        s = -1

if s == -1:
    m = max(m, cnt)
elif s == 1:
    p = max(p, cnt)

print(max(p, m))