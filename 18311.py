import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
go = []
res = 0

for i in range(N):
    if i == 0:
        go.append(arr[0])
        if K < go[0]:
            res = 1
            break
        elif K == go[0]:
            res = 2
            break
    else:
        go.append(arr[i] + go[-1])
        if K < go[-1]:
            res = i + 1
            break
        elif K == go[-1]:
            if i == N - 1:
                res = i + 1
            else:
                res = i + 2
            break

if go[-1] + go[-1] == K:
    print(1)
elif res == 0:
    go[-1] += arr[-1]
    if K < go[-1]:
        res = N
    elif K == go[-1]:
        res = N - 1
    else:
        for i in range(N - 2, -1, -1):
            go[i] = arr[i] + go[i + 1]
            if K < go[i]:
                res = i + 1
                break
            elif K == go[i]:
                if i == 0:
                    res = 1
                else:
                    res = i
                break

    print(res)
else:
    print(res)