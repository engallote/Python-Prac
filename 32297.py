import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

if s.count("gori") >= 1:
    print("YES")
else:
    print("NO")