import sys


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a, b, a / pow(2, b)))

arr.sort(key = lambda x : (x[2], x[0], x[1]))
for i in arr:
    print(i[0], i[1])