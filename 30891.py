import math
import sys

N, R = map(int, sys.stdin.readline().split())
arr = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))

mx, x, y = 0, 0, 0
for i in range(-100, 101):
    for j in range(-100, 101):
        tmp = 0
        for k in range(N):
            if math.sqrt((arr[k][0] - i) ** 2 + (arr[k][1] - j) ** 2) <= R:
                tmp += 1

        if tmp > mx:
            mx = tmp
            x = i
            y = j

print(x, y)