import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(N):
    arr = list(sys.stdin.readline().split())

    tmp = []
    for i in range(2, 5):
        tmp.append(arr[i])

    s = ''.join(tmp)

    if s in dic:
        dic[s] = '?'
    else:
        dic[s] = arr[1]

for _ in range(M):
    arr = list(sys.stdin.readline().split())
    s = ''.join(arr)

    if s in dic:
        print(dic[s])
    else:
        print('!')