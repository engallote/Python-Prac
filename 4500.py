import sys


T = int(sys.stdin.readline())

for _ in range(T):
    arr = list(sys.stdin.readline().rstrip().split())
    name = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    start = arr.index(name)

    start += N - 1
    start %= len(arr)

    print(arr[start])