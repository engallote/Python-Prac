import sys


arr = []
res = 0
for _ in range(10):
    N = int(sys.stdin.readline())
    arr.append(N)

for i in range(10):
    res = 0
    for j in range(10):
        if i == j:
            continue
        res += arr[j]

    if res == arr[i]:
        print(arr[i])
        break