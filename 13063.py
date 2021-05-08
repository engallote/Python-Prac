import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 0 and b == 0 and c == 0:
        break

    sub = a - (b + c)
    need = -1

    for i in range(sub + 1):
        if b + i > c + (sub - i):
            need = i
            break

    print(need)