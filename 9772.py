import sys

while True:
    A, B = map(float, sys.stdin.readline().split())

    if A == 0 or B == 0:
        print("AXIS")
    elif A > 0 and B > 0:
        print("Q1")
    elif A > 0  and B < 0:
        print("Q4")
    elif A < 0 and B > 0:
        print("Q2")
    else:
        print("Q3")

    if A == 0 and B == 0:
        break