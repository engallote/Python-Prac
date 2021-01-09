import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort()

    print(arr[0], arr[-1])