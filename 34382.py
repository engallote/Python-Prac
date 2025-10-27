import sys


N = int(sys.stdin.readline())
arr, m = [], 0
for _ in range(N):
    num = float(sys.stdin.readline())
    arr.append(num)
    m += num

if m != 0:
    m /= N

res = 0
for i in arr:
    if abs(i - m) > 10:
        res += 1

print(res)