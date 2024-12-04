import sys

N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    if a < b:
        if b - a < a - 200 + 243 - b:
            print("Inner circle line")
        elif b - a > a - 200 + 243 - b:
            print("Outer circle line")
        else:
            print("Same")
    else:
        if a - b < 243 - a + b - 200:
            print("Outer circle line")
        elif a - b > 243 - a + b - 200:
            print("Inner circle line")
        else:
            print("Same")