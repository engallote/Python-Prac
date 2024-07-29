import sys


N = int(sys.stdin.readline())
st = sys.stdin.readline().rstrip()

s, ans = 0, "No"
for i in st:
    if i == 'o':
        s += 1
    else:
        s = 0

    if s >= 3:
        ans = "Yes"

print(ans)