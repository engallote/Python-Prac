import sys


arr = list(sys.stdin.readline().rstrip())

for i in range(0, len(arr), 2):
    num = int(arr[i]) * 2

    if num >= 10:
        s = str(num)
        num = int(s[0]) + int(s[1])

    arr[i] = str(num)

res = 0
for i in arr:
    res += int(i)

if res % 10 == 0:
    print("DA")
else:
    print("NE")