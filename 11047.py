N, K = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)

res = 0
for i in range(N):
    if K >= arr[i]:
        res += K // arr[i]
        K %= arr[i]
    if K == 0:
        break

print(res)