import sys


def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        tmp = a
        a = b
        b = tmp

    return gcd(b, a % b)


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
X = int(sys.stdin.readline())

res, cnt = 0, 0
for num in arr:
    if gcd(num, X) == 1:
        res += num
        cnt += 1

print(res / cnt)
