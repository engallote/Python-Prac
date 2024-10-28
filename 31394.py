import sys


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

score = sum(arr) / N

if arr.count(3) > 0:
    print("None")
elif arr.count(5) == N:
    print("Named")
elif 4.5 <= score:
    print("High")
else:
    print("Common")