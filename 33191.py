import sys


N = int(sys.stdin.readline())
w = int(sys.stdin.readline())
p = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if N >= w:
    print("Watermelon")
elif N >= p:
    print("Pomegranates")
elif N >= m:
    print("Nuts")
else:
    print("Nothing")
