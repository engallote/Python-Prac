import sys

N = int(sys.stdin.readline())
arr, res, cnt = {}, [], {}

for i in range(N):
    name, ring = sys.stdin.readline().split()

    if ring == '-':
        continue

    if ring in arr:
        cnt[ring] += 1
        arr[ring] = arr[ring] + " " + name
    else:
        arr[ring] = name
        cnt[ring] = 1

for i in arr.keys():
    if cnt[i] != 2:
        continue
    res.append(arr[i])

print(len(res))
for i in res:
    print(i)