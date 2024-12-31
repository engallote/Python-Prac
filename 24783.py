import sys


N = int(sys.stdin.readline())

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    if a + b == c or a - b == c or a * b == c or a / b == c or b - a == c or b / a == c:
        print("Possible")
    else:
        print("Impossible")