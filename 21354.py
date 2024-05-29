import sys


A, P = map(int, sys.stdin.readline().split())

if A * 7 > P * 13:
    print("Axel")
elif A * 7 == P * 13:
    print("lika")
else:
    print("Petra")