import sys


X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
cnt = 0

while X < N:
    if X % 3 == 0:
        X += 1
    elif X % 3 == 1:
        X *= 2
    else:
        X *= 3
    cnt += 1

print(cnt)