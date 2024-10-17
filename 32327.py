import sys


d = int(sys.stdin.readline())

while True:
    y = sys.stdin.readline().rstrip()

    if y == "":
        break

    if int(y) >= d:
        print(d)
        break

    d += int(y)