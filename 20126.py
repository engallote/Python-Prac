import sys

N, M, S = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort(key=lambda x: x[0])

flag = False
start = 0
if arr[0][0] >= M:
    flag = True

if not flag:
    start = arr[0][0] + arr[0][1]
    for i in range(1, N):
        end = arr[i][0]

        if end - start >= M:
            flag = True
            break

        start = end + arr[i][1]

if flag:
    print(start)
else:
    if S - start >= M:
        print(start)
    else:
        print(-1)