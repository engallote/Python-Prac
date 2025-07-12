import sys


N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip().split())
res = 0

for i in arr:
    if i == "she" or i == "he" or i == "him" or i == "her":
        res += 1

print(res)