import sys


N, M = map(int, sys.stdin.readline().split())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

H = int(sys.stdin.readline())

chk = [[100000000 for _ in range(M)] for _ in range(N)]
chk[0][0] = arr[0][0]

for i in range(N):
    for j in range(M):
        if j - 1 >= 0:
            chk[i][j] = min(chk[i][j], chk[i][j - 1] + arr[i][j])
        if i - 1 >= 0 :
            chk[i][j] = min(chk[i][j], chk[i - 1][j] + arr[i][j])

if chk[N - 1][M - 1] <= H:
    print("YES")
    print(chk[N - 1][M - 1])
else:
    print("NO")