import sys

N = int(sys.stdin.readline())
G = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.append(G)
arr.sort(reverse=True)

print(arr.index(G) + 1)