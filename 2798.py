N, M = map(int, input().split())
arr = list(map(int, input().split()))
maxNum = 0

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] <= M:
                maxNum = max(maxNum, arr[i] + arr[j] + arr[k])

print(maxNum)