import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(sys.stdin.readline().rstrip()))

flag = True

x = 1
y = M // 2

while x < N - 1:
    flag = True
    if M % 2 == 0:
        if arr[x][y] == 'B' or arr[x][y - 1] == 'B' or arr[x][y - 2] == 'B' or arr[x][y + 1] == 'B':
            flag = False
    else:
        if arr[x][y] == 'B' or arr[x][y - 1] == 'B' or arr[x][y + 1] == 'B':
            flag = False
    if flag:
        break
    x += 1

for i in range(N):
    for j in range(M):
        arr[i][j] = 'B'

if flag:
    print("YES")

    if M % 2 == 0:
        arr[x][y] = arr[x][y - 1] = 'Y'
        arr[x][y - 2] = arr[x][y + 1] = 'W'
    else:
        arr[x][y] = 'Y'
        arr[x][y - 1] = arr[x][y + 1] = 'W'

    for i in range(N):
        print(''.join(arr[i]))
else:
    print("NO")