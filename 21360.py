import sys


N = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip()

res, pre = 100000000, -1
for i in range(N):
    if arr[i] == '.':
        if pre == -1:
            pre = i
        else:
            res = min(res, i - pre - 1)

        pre = i
        if res == 0:
            break

print(res)