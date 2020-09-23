import sys

N = int(sys.stdin.readline().rstrip())
arr = map(int, sys.stdin.readline().rstrip().split())
min = 1000000000
max = -1000000000

for i in arr:
    if min > i:
        min = i
    if max < i:
        max = i

print("%d %d" % (min, max))