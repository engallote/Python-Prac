import sys


N = int(sys.stdin.readline())
dic = dict()
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a in dic:
        dic[a] += b
    else:
        dic[a] = b

print(len(dic))
for i in dic:
    print(i, dic[i])