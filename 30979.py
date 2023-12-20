import sys

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

if sum(arr) >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")