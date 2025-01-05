import sys


A = sys.stdin.readline().rstrip()
B = list(sys.stdin.readline().rstrip().split())

for i in range(len(A)):
    if A[i] in B:
        print(A[i].lower(), end='')
    else:
        print(A[i], end='')
