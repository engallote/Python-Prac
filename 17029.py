import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    tmp = list(sys.stdin.readline().rstrip().split())
    arr.append(tmp[2:])

res = 0
for i in range(N):
    for j in range(i + 1, N):
        mx = 0
        for a in arr[i]:
            for b in arr[j]:
                if a == b:
                    mx += 1
        res = max(res, mx + 1)

print(res)