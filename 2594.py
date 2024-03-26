import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    d = a // 100
    a %= 100
    a += d * 60

    d = b // 100
    b %= 100
    b += d * 60

    arr.append((a - 10, b + 10))

arr.sort(key=lambda x: (x[0], x[1]))

pe, res = 600, 0
for i in range(N):
    s, e = arr[i][0], arr[i][1]
    res = max(res, s - pe)
    pe = max(pe, e)

end = 60 * 22
res = max(res, end - pe)

print(res)