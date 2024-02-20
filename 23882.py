import sys


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = [arr]
cnt = 0

for j in range(N - 1, 0, -1):
    mx = max(arr[:j + 1])
    idx = arr.index(mx)
    if idx != j:
        cnt += 1

        arr[idx] = arr[j]
        arr[j] = mx

        if cnt == K:
            print(*arr)
            break

if cnt < K:
    print(-1)