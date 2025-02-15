import sys


w = int(sys.stdin.readline())
l = int(sys.stdin.readline())
h = int(sys.stdin.readline())

if min(w, l) / h >= 2 and max(w, l) / min(w, l) <= 2:
    print("good")
else:
    print("bad")