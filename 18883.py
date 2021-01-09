import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
cnt = 1
for _ in range(N):
    for i in range(M):
        if i == M - 1:
            print(cnt, end='')
        else:
            print(cnt, end=' ')
        cnt += 1
    print()
