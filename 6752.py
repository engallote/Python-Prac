import sys

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

res, time = 0, 0
for i in arr:
    if time + i <= T:
        time += i
        res += 1
    else:
        break

print(res)