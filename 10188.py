import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    
    for _ in range(b):
        for _ in range(a):
            print("X", end='')
        print()
    
    print()
