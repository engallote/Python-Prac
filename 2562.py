maxNum = -1
maxIdx = -1

for i in range(1, 10):
    num = int(input())
    if num > maxNum:
        maxNum = num
        maxIdx = i
print(maxNum)
print(maxIdx)