import sys


B, N, M = map(int, sys.stdin.readline().split())
arr = {}
for _ in range(N):
    item, co = sys.stdin.readline().split()
    arr[item] = int(co)

res = 0
for _ in range(M):
    res += arr[sys.stdin.readline().rstrip()]

if res > B:
    print("unacceptable")
else:
    print("acceptable")