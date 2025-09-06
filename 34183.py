import sys


N, M, A, B = map(int, sys.stdin.readline().split())
if M >= N * 3:
    print(0)
else:
    print((N * 3 - M) * A + B)