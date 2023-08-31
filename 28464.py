import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

s, b, who = 0, 0, 1
l, r = 0, N - 1

while l <= r:
    if who == 0:
        s += arr[l]
        l += 1
    else:
        b += arr[r]
        r -= 1

    who = 1 - who

print(s, b)