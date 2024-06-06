import sys


S = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

res = 250

S -= A
if S > 0:
    res += S // B * 100
    if S % B > 0:
        res += 100

print(res)