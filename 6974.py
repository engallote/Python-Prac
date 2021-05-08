import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a = int(sys.stdin.readline().rstrip())
    b = int(sys.stdin.readline().rstrip())

    print(a // b)
    print(a % b)
    print()