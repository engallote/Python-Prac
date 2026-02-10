import sys

N = int(sys.stdin.readline())
res = N.bit_length()
arr = [1, 2, 4, 8, 16, 32, 64]

for i in arr:
    if i >= res:
        res = i
        break

if res <= 1:
    print(res, "bit")
else:
    print(res, "bits")
