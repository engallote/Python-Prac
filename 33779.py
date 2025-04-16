import sys


N = sys.stdin.readline().rstrip()
l, r, c = 0, len(N) - 1, 0

while l <= r:
    if N[l] != N[r]:
        c = 1
        break
    l += 1
    r -= 1

if c == 0:
    print("beep")
else:
    print("boop")