import sys


N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
dic = dict()

for i in range(N):
    if arr[i] in dic:
        continue
    else:
        dic[arr[i]] = i

sorted(dic.items())

for _ in range(M):
    num = int(sys.stdin.readline())

    if num in dic:
        print(dic[num])
    else:
        print(-1)