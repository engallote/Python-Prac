import sys

N = int(sys.stdin.readline().rstrip())
start = False
res, pre = 0, -1
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())

    if start:
        start = False
        res += num - pre
    else:
        start = True
        pre = num

if start:
    print("still running")
else:
    print(res)