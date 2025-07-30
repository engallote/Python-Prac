import sys


N = int(sys.stdin.readline())

for i in range(1, N + 1):
    a, b = map(int, sys.stdin.readline().split())

    print("Data Set %d:" %i)

    if a <= b:
        print("no drought")
    else:
        k, cnt = 1, 0
        while True:
            if b * k < a <= b * (k * 5):
                break
            cnt += 1
            k *= 5
        print("mega " * cnt, end='')
        print("drought")
    print()