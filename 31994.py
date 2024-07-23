import sys


mx, ans = -1, ""
for _ in range(7):
    a, b = sys.stdin.readline().split()

    if int(b) > mx:
        mx = int(b)
        ans = a

print(ans)