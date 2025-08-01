import sys


N = int(sys.stdin.readline())

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 != 0:
        print("Dead")
    elif i % 3 != 0 and i % 5 == 0:
        print("Man")
    elif i % 3 == 0 and i % 5 == 0:
        print("DeadMan")
    else:
        print(i, end=' ')