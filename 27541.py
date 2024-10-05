import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

if s[-1] == "G":
    print(s[0:-1])
else:
    s += "G"
    print(s)