import sys


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt, a, b = 0, 0, 0
for i in range(N - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            cnt += 1
            if cnt == K:
                a = arr[j + 1]
                b = arr[j]
                break
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp
    if cnt == K:
        break

if cnt == K:
    print(a, b)
else:
    print(-1)