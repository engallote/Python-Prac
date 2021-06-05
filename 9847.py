import sys

a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
A, B, C, D = [], [], [], []

for _ in range(a):
    A.append(int(sys.stdin.readline()))

for _ in range(b):
    B.append(int(sys.stdin.readline()))

for _ in range(c):
    C.append(int(sys.stdin.readline()))

for _ in range(d):
    D.append(int(sys.stdin.readline()))

flag = False
for i in A:
    if flag:
        break
    for j in B:
        if flag:
            break
        for k in C:
            if flag:
                break
            for l in D:
                if i + j + k + l == 0:
                    print(i, j, k, l)
                    flag = True
                    break
                if flag:
                    break