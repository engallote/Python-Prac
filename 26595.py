import sys


N = int(sys.stdin.readline())
a, pa, b, pb = map(int, sys.stdin.readline().split())

A, B, res = 0, 0, 0
for i in range(N + 1):
    aa = i // pa
    bb = (N - i) // pb

    if a * aa + b * bb > res:
        res = a * aa + b * bb
        A = aa
        B = bb

print(A, B)