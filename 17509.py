import sys

res, time = 0, 0
arr = [[0 for x in range(2)] for x in range(11)]

for i in range(11):
    arr[i][0], arr[i][1] = map(int, sys.stdin.readline().rstrip().split())

arr.sort(key= lambda x: (x[0], x[1]))

for i in range(11):
    time += arr[i][0]
    res += time + 20 * arr[i][1]

print(res)