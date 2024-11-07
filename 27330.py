import sys


N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

score = 0
for i in range(N):
    score += arr1[i]

    if score in arr2:
        score = 0

print(score)