import sys


T = int(sys.stdin.readline())

for _ in range(T):
    g1, s1, b1, g2, s2, b2 = map(int, sys.stdin.readline().split())

    ans = "none"
    res = 0
    if g1 + s1 + b1 > g2 + s2 + b2:
        ans = "count"
        res += 1
    if g1 > g2 or (g1 == g2 and s1 > s2) or (g1 == g2 and s1 == s2 and b1 > b2):
        ans = "color"
        res += 1

    if res > 1:
        ans = "both"

    print(g1, s1, b1, g2, s2, b2)
    print(ans)
    print()