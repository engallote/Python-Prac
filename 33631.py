import sys


F, C, E, B = map(int, sys.stdin.readline().split())
f, c, e, b = map(int, sys.stdin.readline().split())
Q = int(sys.stdin.readline())

co, ch, fl, eg, bu = 0, 0, 0, 0, 0
for _ in range(Q):
    a, i = map(int, sys.stdin.readline().split())

    if a == 1:
        if i * f <= F and i * c <= C and i * e <= E and i * b <= B:
            co += i
            F -= i * f
            C -= i * c
            E -= i * e
            B -= i * b
            print(co)
        else:
            print("Hello, siumii")
    elif a == 2:
        F += i
        print(F)
    elif a == 3:
        C += i
        print(C)
    elif a == 4:
        E += i
        print(E)
    else:
        B += i
        print(B)
