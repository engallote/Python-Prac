import sys


while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    arr = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline()))

    arr.reverse()
    print(*arr, sep='\n')
    print(0)