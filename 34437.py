import sys


N = int(sys.stdin.readline())
cnt = 0

while N > 1:
    if N % 2 == 0:
        N //= 2
    else:
        N += N * 2 + 1
    cnt += 1

print(cnt)