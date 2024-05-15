import sys

res = 91
for i in range(3):
    N = int(sys.stdin.readline())

    if i % 2 == 0:
        res += N * 1
    else:
        res += N * 3

print("The 1-3-sum is", res)