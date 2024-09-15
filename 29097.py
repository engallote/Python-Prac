import sys


arr = list(map(int, sys.stdin.readline().split()))
j = arr[0] * arr[3]
r = arr[1] * arr[4]
s = arr[2] * arr[5]

dic = {"Joffrey": j, "Robb": r, "Stannis": s}
d = sorted(dic.items(), key= lambda x : (x[1], x[0]))
mx = max(j, r, s)

for i in d:
    if i[1] != mx:
        continue
    print(i[0], end=' ')