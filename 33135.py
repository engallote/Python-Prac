import sys


arr = list(sys.stdin.readline().rstrip())
arr.sort()
res = 1

for i in range(1, len(arr)):
    if arr[i - 1] == arr[i]:
        continue

    res += 1

print(len(arr) - res)