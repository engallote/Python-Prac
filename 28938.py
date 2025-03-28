import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
l, r = 0, 0

for i in arr:
    if i == -1:
        l += 1
    elif i == 1:
        r += 1

if l > r:
    print("Left")
elif l < r:
    print("Right")
else:
    print("Stay")