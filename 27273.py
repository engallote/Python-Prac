import sys


N = int(sys.stdin.readline())
arr = [1] * (N + 1)

mx, cnt = 1, 1
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        arr[j] += 1
        if arr[j] > cnt:
            mx = j
            cnt = arr[j]

print(mx)
print(cnt)