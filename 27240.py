import sys


N, a, b = map(int, sys.stdin.readline().split())
s, t = map(int, sys.stdin.readline().split())

if (1 <= s <= a and 1 <= t <= a) or (b <= s <= N and b <= t <= N):
    print("Outside")
elif a + 1 <= s <= b - 1 and a + 1 <= t <= b - 1:
    print("City")
else:
    print("Full")