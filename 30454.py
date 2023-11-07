import sys

N, L = map(int, sys.stdin.readline().split())

mx, cnt = 0, 0
for _ in range(N):
    arr = list(sys.stdin.readline().rstrip())

    tmp, pre = 0, '0'
    for j in arr:
        if j == '1':
            if pre == j:
                continue
            else:
                tmp += 1
        pre = j

    if tmp > mx:
        mx = tmp
        cnt = 1
    elif tmp == mx:
        cnt += 1

print(mx, cnt)