import sys


x, y, z = map(int, sys.stdin.readline().split())
if 90 <= x * 0.25 + y * 0.25 + z * 0.5 <= 100:
    print("A")
elif 80 <= x * 0.25 + y * 0.25 + z * 0.5 < 90:
    print("B")
elif 70 <= x * 0.25 + y * 0.25 + z * 0.5 < 80:
    print("C")
elif 60 <= x * 0.25 + y * 0.25 + z * 0.5 < 70:
    print("D")
else:
    print("F")