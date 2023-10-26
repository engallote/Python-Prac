import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    num = i * 100 // N

    if 0 <= num <= 4:
        print("1", end=' ')
    elif 5 <= num <= 11:
        print("2", end=' ')
    elif 12 <= num <= 23:
        print("3", end=' ')
    elif 24 <= num <= 40:
        print("4", end=' ')
    elif 41 <= num <= 60:
        print("5", end=' ')
    elif 61 <= num <= 77:
        print("6", end=' ')
    elif 78 <= num <= 89:
        print("7", end=' ')
    elif 90 <= num <= 96:
        print("8", end=' ')
    else:
        print("9", end=' ')