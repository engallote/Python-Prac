import sys

N, D = map(int, sys.stdin.readline().split())
monster, eq = [], []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        monster.append(b)
    else:
        eq.append(b)

monster.sort(reverse=True)
eq.sort(reverse=True)

res = len(eq)
while len(monster) > 0:
    if max(monster) < D:
        res += len(monster)
        break

    m = monster.pop()
    while len(eq) > 0 and D <= m:
        D *= eq.pop()
    if D > m:
        D += m
        res += 1
    else:
        break

print(res)