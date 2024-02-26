import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dic = {}

for i in range(N):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1

d = sorted(dic.items(), key=lambda x: -x[1])

mx, s = 0, 0
for i, j in d:
    if mx == 0:
        mx = j
    else:
        s += j

if mx - s >= 2:
    print("NO")
else:
    print("YES")