import sys


N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip().split())

for i in range(N):
    if i < N - 1:
        print(arr[i], end='DORO ')
    else:
        print(arr[i], end='DORO')