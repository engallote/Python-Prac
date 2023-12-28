import sys

N = int(sys.stdin.readline())
res, cnt = 1000000000, 0
arr = []
for _ in range(N):
    state, cost = sys.stdin.readline().split()
    arr.append((state, cost))

    if state == 'jinju':
        res = min(res, int(cost))

for i in arr:
    if int(i[1]) > res:
        cnt += 1

print(res)
print(cnt)