import sys


N = int(sys.stdin.readline())


for _ in range(N):
    for _ in range(N):
        print("@@@@@", end='')
    print()

for _ in range(N * 4):
    for _ in range(N):
        print("@", end='')
    print()