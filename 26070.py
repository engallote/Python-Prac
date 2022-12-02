import sys

A, B, C = map(int, sys.stdin.readline().split())
X, Y, Z = map(int, sys.stdin.readline().split())

res, tmp = 0, min(A, X)
A -= tmp
X -= tmp
res += tmp

tmp = min(B, Y)
B -= tmp
Y -= tmp
res += tmp

tmp = min(C, Z)
C -= tmp
Z -= tmp
res += tmp

flag = True
while flag:
    flag = False
    if X >= 0:
        tmp = min(A, X)
        if tmp != 0:
            flag = True
        X -= tmp
        A -= tmp
        res += tmp
        Y += X // 3
        X %= 3
        if Y >= 3:
            flag = True
    if Y >= 0:
        tmp = min(B, Y)
        if tmp != 0:
            flag = True
        B -= tmp
        Y -= tmp
        res += tmp
        Z += Y // 3
        Y %= 3
        if Z >= 3:
            flag = True
    if Z >= 0:
        tmp = min(C, Z)
        if tmp != 0:
            flag = True
        C -= tmp
        Z -= tmp
        res += tmp
        X += Z // 3
        Z %= 3
        if X >= 3:
            flag = True

    # print(A, B, C)
    # print(X, Y, Z)
    # print("==========")


print(res)