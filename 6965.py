import sys


N = int(sys.stdin.readline())

for _ in range(N):
    arr = list(sys.stdin.readline().rstrip().split())

    for i in arr:
        if len(i) == 4:
            print("****", end=' ')
        else:
            print(i, end=' ')
    print()
    print()