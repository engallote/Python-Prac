import sys


N = int(sys.stdin.readline())
chk = [False for _ in range(100)]
arr = [0 for _ in range(N)]
arr[0], arr[1] = 1, 2
chk[0] = chk[1] = True

for i in range(2, 100):
    if chk[i]:
        continue

    for j in range(i + i, 100, i):
        chk[j] = True

for i in range(2, N - 1):
    arr[i] = i + 1

for i in range(5, 100):
    if arr[N - 2] < i and not chk[i]:
        arr[N - 1] = i
        break

print(N)
for i in range(N):
    print(arr[i], end=' ')