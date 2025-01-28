import sys


N = int(sys.stdin.readline())

if 1 <= N <= 9:
    print(1)
else:
    ans = 0
    for i in range(2, 10):
        if 1 <= N // i <= 9 and N % i == 0:
            ans = 1
            break
    print(ans)