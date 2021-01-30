import sys


A, B = int(sys.stdin.readline()), int(sys.stdin.readline())
cnt, nxt = 2, A - B

while True:
    A = B
    B = nxt
    cnt += 1

    if A < B:
        break

    nxt = A - B

print(cnt)