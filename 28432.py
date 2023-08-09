import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline())
ans = []
for i in range(M):
    ans.append(sys.stdin.readline().rstrip())

start, end = '*', '*'
for i in range(N):
    if arr[i] == '?':
        if 0 <= i - 1:
            start = str(arr[i - 1])[-1]
        if i + 1 < N:
            end = str(arr[i + 1])[0]
        break

for i in ans:
    if arr.count(i) != 0:
        continue
    if start == i[0] and end == i[-1]:
        print(i)
        break
    elif start == '*' and end == i[-1]:
        print(i)
        break
    elif start == i[0] and end == '*':
        print(i)
        break
    elif start == '*' and end == '*':
        print(i)
        break
