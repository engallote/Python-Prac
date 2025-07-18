import sys


a, b, c, d, e, f = map(int, sys.stdin.readline().split())
bb = b * 5
cc = c * 10
dd = d * 20
ee = e * 50
ff = f * 100

arr = [(a, a, 1), (bb, b, 5), (cc, c, 10), (dd, d, 20), (ee, e, 50), (ff, f, 100)]
arr.sort(key=lambda x:(-x[0], x[1]))
print(arr[0][2])