import sys


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1

    print(*arr[a:b], sep='\n')