import sys

def dfs(idx):
    if idx == len(arr2):
        global res
        tmp = ''.join(arr)
        num = int(tmp, 2)
        num2 = int(num ** 0.5) ** 2

        if num == num2:
            res = tmp
        return

    arr[arr2[idx]] = '0'
    dfs(idx + 1)
    arr[arr2[idx]] = '1'
    dfs(idx + 1)
    arr[arr2[idx]] = '?'


N = int(sys.stdin.readline())

for i in range(1, N + 1):
    arr = list(sys.stdin.readline().rstrip())
    arr2 = []
    for j in range(len(arr)):
        if arr[j] == '?':
            arr2.append(j)

    res = ''
    dfs(0)
    print("Case #%d: %s" %(i, res))
