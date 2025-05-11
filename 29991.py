import sys


D, C, R = map(int, sys.stdin.readline().split())
c, r, res = [], [], 0

for _ in range(C):
    c.append(int(sys.stdin.readline()))

for _ in range(R):
    r.append(int(sys.stdin.readline()))

for i in range(C):
    if D >= c[i]:
        D -= c[i]
        res += 1
    else:
        while len(r) > 0:
            D += r.pop(0)
            res += 1
            if D >= c[i]:
                break

        if D >= c[i]:
            D -= c[i]
            res += 1
        else:
            break

res += len(r)
print(res)