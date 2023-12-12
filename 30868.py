import sys

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    div, mod = num // 5, num % 5

    for _ in range(div):
        print('++++', end=' ')

    print('|'*mod)