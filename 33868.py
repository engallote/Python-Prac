import sys


N = int(sys.stdin.readline())
arr = [1, 2, 3, 4, 5, 6, 7]
mt, mb = 0, 10000000000

for _ in range(N):
    T, B = map(int, sys.stdin.readline().split())

    if T > mt:
        mt = T
    if B < mb:
        mb = B

print(arr[mt * mb % 7])