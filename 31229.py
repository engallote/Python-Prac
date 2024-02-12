import sys


N = int(sys.stdin.readline())
arr, chk = [], [False for _ in range(100000)]

for i in range(2, 100000):
    if chk[i]:
        continue
    arr.append(i)
    for j in range(i + i, 100000, i):
        chk[j] = True

idx = 0
for i in range(N):
    print(arr[idx], end=' ')
    idx += 1