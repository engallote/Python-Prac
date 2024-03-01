import sys

N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())
track = sys.stdin.readline().rstrip()

print(arr.count(track))