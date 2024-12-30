import sys


N = int(sys.stdin.readline())
start, cnt = 0, 0

for _ in range(N):
    num = int(sys.stdin.readline())
    if start == 0:
        start = num
        cnt = 0

    if num % start == 0 and cnt > 0:
        print(num)
        start = 0

    cnt += 1