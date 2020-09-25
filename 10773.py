import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))