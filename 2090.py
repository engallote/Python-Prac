import sys


def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        tmp = a
        a = b
        b = tmp
    return gcd(b, a % b)


def LCM(a, b):
    res = (a * b) // gcd(a, b)
    return res


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lcm = arr[0]
for i in range(1, N):
    lcm = LCM(lcm, arr[i])

num = 0
for i in range(N):
    num += lcm // arr[i]

g = gcd(lcm, num)
num //= g
lcm //= g

print("%d/%d" % (lcm, num))