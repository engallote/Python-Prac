import sys


N = int(sys.stdin.readline())

num = 0
res = []

for _ in range(N):
    arr = list(sys.stdin.readline().split())

    if num < int(arr[0]):
        num = int(arr[0])
        res = []
        for i in range(1, len(arr)):
            res.append(arr[i])

print(num)
for i in res:
    print(i)