import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
arr = [i for i in sys.stdin.readline().rstrip().split() if int(i) < X]

print(' '.join(arr))