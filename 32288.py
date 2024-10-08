import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

for i in s:
    if i == "I":
        print('i', end='')
    else:
        print("L", end='')