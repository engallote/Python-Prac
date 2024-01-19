import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    s = list(sys.stdin.readline().split())
    tmp = 0
    for j in range(int(s[0])):
        tmp += int(s[j + 1])

    arr.append(tmp)

arr.sort()

res = 0
for i in range(N):
    if i > 0:
        arr[i] += arr[i - 1]
    res += arr[i]

print(res)