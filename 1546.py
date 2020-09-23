N = int(input())

arr = map(int, input().split())
arr = sorted(arr)

maxNum = arr[len(arr)-1]
sum = 0.0

for i in arr:
    sum += i / maxNum * 100

sum /= N
print(sum)