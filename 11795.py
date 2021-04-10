import sys

N = int(sys.stdin.readline().rstrip())
sumList = [0, 0, 0]
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    minNum = 1000000000

    for i in range(0, 3):
        sumList[i] += arr[i]
        minNum = min(minNum, sumList[i])

    if minNum >= 30:
        print(minNum)
        sumList[0] -= minNum
        sumList[1] -= minNum
        sumList[2] -= minNum
    else:
        print("NO")