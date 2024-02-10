import sys


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt, num = 0, -1
for i in range(1, N):
    loc = i - 1
    item = arr[i]

    while 0 <= loc and item < arr[loc]:
        cnt += 1
        if cnt == K:
            num = arr[loc]
        arr[loc + 1] = arr[loc]
        loc -= 1

    if loc + 1 != i:
        arr[loc + 1] = item
        cnt += 1
        if cnt == K:
            num = arr[loc]

print(num)