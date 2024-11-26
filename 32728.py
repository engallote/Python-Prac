import sys


N, K = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()
A, B, C = [], [], []

for i in s:
    if i == 'r':
        if len(B) < K:
            B.append(i)
        else:
            if len(C) < K:
                C.append(i)
            else:
                A.append(i)
    elif i == 'p':
        if len(C) < K:
            C.append(i)
        else:
            if len(A) < K:
                A.append(i)
            else:
                B.append(i)
    else:
        if len(A) < K:
            A.append(i)
        else:
            if len(B) < K:
                B.append(i)
            else:
                C.append(i)

print(*A, sep="")
print(*B, sep="")
print(*C, sep="")