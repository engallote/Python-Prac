import sys


N = int(sys.stdin.readline())
dic = dict()
mx = 0
for _ in range(N):
    num = int(sys.stdin.readline())

    if num in dic:
        dic[num] += 1
        mx = max(mx, dic[num])
    else:
        dic[num] = 1
        mx = max(mx, dic[num])

print(mx)