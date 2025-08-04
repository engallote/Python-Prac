import sys


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    s = sys.stdin.readline()

    if s in arr:
        continue
    else:
        arr.append(s)

print(len(arr))