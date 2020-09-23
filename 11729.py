def hanoi(N, A, B, C):
    if (N, A, C) in arr:
        return arr[(N, A, C)]
    if N == 1:
        s = f'{A} {C}'
    else:
        s = f'{hanoi(N - 1, A, C, B)}\n{A} {C}\n{hanoi(N - 1, B, A, C)}'
        arr[(N, A, C)] = s
    return s


N = int(input())
arr = {}
print(2 ** N - 1)
if N == 1:
    print("1 3")
elif N == 2:
    print("1 2")
    print("1 3")
    print("2 3")
else:
    print(hanoi(N, 1, 2, 3))