import sys


Q = int(sys.stdin.readline())
arr = [0, 0, 0, 0, 0]

for _ in range(Q):
    n = int(sys.stdin.readline()) - 1
    arr[n] = 1

res = "NO"
for i in arr:
    if i == 0:
        res = "YES"
        break

print(res)