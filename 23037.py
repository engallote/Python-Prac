import sys


s = sys.stdin.readline().rstrip()
res = 0

for i in s:
    num = int(i)**5
    res += num

print(res)