import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
res = 0

if N < len(s):
    print("Impossible")
else:
    for i in s:
        res += ord(i) - 96
    print(res)