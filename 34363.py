import sys


S = int(sys.stdin.readline())
D = float(sys.stdin.readline())
T = float(sys.stdin.readline())

speed = S * 5280/3600

if speed * T >= D:
    print("MADE IT")
else:
    print("FAILED TEST")