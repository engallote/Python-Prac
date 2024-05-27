import sys

A = float(sys.stdin.readline())
B = float(sys.stdin.readline())
res = A / B ** 2
if res < 18.5:
    print("Underweight")
elif 18.5 <= res <= 25:
    print("Normal weight")
else:
    print("Overweight")