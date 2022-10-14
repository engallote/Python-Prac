import sys

N = int(sys.stdin.readline())
P = int(sys.stdin.readline())

num = P

if N >= 5:
    num = P - 500
if N >= 10:
    num = min(num, P * 0.9)
if N >= 15:
    num = min(num, P - 2000)
if N >= 20:
    num = min(num, P * 0.75)

if num < 0:
    num = 0

print(int(num))