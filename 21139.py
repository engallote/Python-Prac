import sys


def solve(idx):
    if idx == K:
        ff = 0
        for i in range(N):
            tmp = 0
            for j in range(K):
                if arr[i][j] != ret[j]:
                    tmp += 1
            ff = max(ff, tmp)
        return ff

    tmp = solve(idx + 1)
    ret[idx] = 'F'
    tmp = min(tmp, solve(idx + 1))
    ret[idx] = 'T'
    return tmp

N, K = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
ret = ['T' for _ in range(K)]
res = solve(0)

print(K-res)