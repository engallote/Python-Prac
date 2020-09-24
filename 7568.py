N = int(input())
arr = [[0] * 2 for _ in range(N)]

for i in range(N):
    arr[i][0], arr[i][1] = map(int, input().split())

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                rank += 1
    print(rank, end=" ")