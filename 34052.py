import sys


res = 0
for _ in range(4):
    num = int(sys.stdin.readline())
    res += num

if 1800 >= res + 300:
    print("Yes")
else:
    print("No")