import sys


N = int(sys.stdin.readline())
res, arr = 0, {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    res = 0

    for i in s:
        if i in arr.keys():
            res += arr[i]

    print(res)