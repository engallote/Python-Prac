import sys


N = int(sys.stdin.readline())
if N % 2 != 0:
    N += 1
arr = list(sys.stdin.readline().rstrip())

if arr.count('O') >= N // 2:
    print("Yes")
else:
    print("No")