import sys


N, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
wait = [0 for _ in range(M)]
for i in arr:
    m, idx = 100000000000, 0
    for j in range(M):
        if wait[j] < m:
            m = wait[j]
            idx = j
    wait[idx] += i

koi = min(wait)

if koi <= K:
    print("WAIT")
else:
    print("GO")