import sys

N, M, K = map(int, sys.stdin.readline().split())

res = 0
for _ in range(N):
    arr = list(sys.stdin.readline().rstrip())
    for j in range(M):
        if arr[j] == '0':
            cnt = 0
            for k in range(j, M):
                if arr[k] == '1':
                    j = k
                    break
                else:
                    cnt += 1
                if cnt == K:
                    break

            if cnt == K:
                res += 1

print(res)