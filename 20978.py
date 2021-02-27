import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

arr = set()

for i in a:
    if b.count(i) > 0:
        arr.add(i)

res = sorted(arr)
for i in res:
    print(i)
