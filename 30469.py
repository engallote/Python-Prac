import sys

A, B, N = map(int, sys.stdin.readline().split())
chk = [False for _ in range(100)]
chk[0] = chk[1] = True

for i in range(2, 100):
    if chk[i]:
        continue
    for j in range(i + i, 100, i):
        chk[j] = True

if B // 10 % 2 == 0 or B // 10 == 5:
    print("-1")
else:
    arr = [0 for _ in range(N)]
    arr[0], arr[1], arr[N - 2], arr[N - 1] = A // 10, A % 10, B // 10, B % 10
    curLen = 2
    for i in range(2, N):
        if arr[i] != 0:
            break
        for j in range(1, 10):
            if not chk[arr[i - 1] * 10 + j]:
                arr[i] = j
                break

    if chk[arr[N - 3] * 10 + arr[N - 2]]:
        for i in range(N - 3, 2, -1):
            if not chk[arr[i] * 10 + arr[i + 1]]:
                break
            for j in range(1, 10):
                if not chk[j * 10 + arr[i + 1]]:
                    arr[i] = j
                    break

    for i in arr:
        print(i, end='')
