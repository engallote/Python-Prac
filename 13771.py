import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    arr.append(float(sys.stdin.readline().rstrip()))

arr = sorted(arr)

print('%.2f' % arr[1])