import sys


def calc(idx, sum):
    if idx == N:
        global maxNum, minNum
        maxNum = max(maxNum, sum)
        minNum = min(minNum, sum)
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                calc(idx + 1, sum + arr[idx])
            elif i == 1:
                calc(idx + 1, sum - arr[idx])
            elif i == 2:
                calc(idx + 1, sum * arr[idx])
            else:
                calc(idx + 1, int(sum / arr[idx]))
            op[i] += 1


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
maxNum, minNum = -100000000000, 100000000000

calc(1, arr[0])

print(maxNum)
print(minNum)