import sys


N = int(sys.stdin.readline())

for _ in range(N // 5):
    print("V", end='')

for _ in range(N % 5):
    print("I", end='')
