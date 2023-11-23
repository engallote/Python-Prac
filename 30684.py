import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    name = sys.stdin.readline().rstrip()

    if len(name) == 3:
        arr.append(name)

arr.sort()
print(arr[0])