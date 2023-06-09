import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

time = 0
for i in arr:
    time += i
    time += 8

time -= 8
print(time // 24, time % 24)