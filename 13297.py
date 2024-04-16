import sys


N = int(sys.stdin.readline())

for _ in range(N):
    num = sys.stdin.readline().rstrip()
    print(len(num))