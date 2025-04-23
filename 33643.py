import sys


N = int(sys.stdin.readline())
arr = ["keys", "wallet", "phone"]

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    if s in arr:
        arr.remove(s)

if len(arr) == 0:
    print("ready")
else:
    arr.sort()
    print(*arr, sep='\n')