import sys

N = int(sys.stdin.readline())

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    div = (len(arr) - 1) / 2
    dic = dict()
    flag = False
    ans = 0

    for i in range(1, arr[0] + 1):
        if arr[i] in dic:
            dic[arr[i]] += 1

            if dic[arr[i]] > div:
                ans = arr[i]
                flag = True
                break
        else:
            dic[arr[i]] = 1

    if flag:
        print(ans)
    else:
        print("SYJKGW")

