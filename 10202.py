import sys

T = int(sys.stdin.readline())

for _ in range(T):
    arr = list(sys.stdin.readline().split())
    N = int(arr[0])
    res, cnt = 0, 0

    for i in range(1, N + 1):
        if arr[i] == 'X':
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 0

    res = max(res, cnt)
    print("The longest contiguous subsequence of X's is of length %d" %res)