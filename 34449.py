import sys


d = float(sys.stdin.readline()) * 3.14159
w = float(sys.stdin.readline())
n = float(sys.stdin.readline())

if d >= w * n:
    print("YES")
else:
    print("NO")