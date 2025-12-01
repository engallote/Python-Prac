import sys


N = int(sys.stdin.readline())

if N < 100000:
    print(int(N * (5 / 100)), int(N - (N * (5 / 100))))
elif 100000 <= N < 500000:
    print(int(N * (10 / 100)), int(N - (N * (10 / 100))))
elif 500000 <= N < 1000000:
    print(int(N * (15 / 100)), int(N - (N * (15 / 100))))
else:
    print(int(N * (20 / 100)), int(N - (N * (20 / 100))))