import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
num = [0 for _ in range(10)]

res, l, r = 0, 0, 0
candy = []
while l <= r:
    if arr[r] in candy:
        if len(candy) <= 2:
            res = max(res, r - l + 1)
        num[arr[r]] += 1
        if r < N - 1:
            r += 1
        else:
            break
    else:
        if len(candy) < 2:
            candy.append(arr[r])
            num[arr[r]] += 1
            if r < N - 1:
                r += 1
            else:
                break
        else:
            while num.count(0) <= 8:
                num[arr[l]] -= 1
                if num[arr[l]] == 0:
                    candy.remove(arr[l])
                l += 1

if len(candy) <= 2:
    res = max(res, r - l + 1)
print(res)