import sys


N = sys.stdin.readline().rstrip()
s, e, res = 0, 0, 0
for i in range(len(N)):
    if N[i] == "0":
        continue
    s = i
    break

for i in range(len(N) - 1, -1, -1):
    if N[i] == "0":
        continue
    e = i
    break

for i in range(s, e):
    if N[i] == "0":
        res += 1

print(res)