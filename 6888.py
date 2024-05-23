import sys

X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())

for i in range(X, Y + 1, 60):
    print("All positions change in year", i)