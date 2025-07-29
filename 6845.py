import sys


N = int(sys.stdin.readline())

for _ in range(N):
    year, month, day = map(int, sys.stdin.readline().split())

    if 2007 - year > 18:
        print("Yes")
    elif 2007 - year == 18:
        if month < 2 or (month == 2 and day <= 27):
            print("Yes")
        else:
            print("No")
    else:
        print("No")