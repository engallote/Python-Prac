import sys

N = int(sys.stdin.readline())
d = {}

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    x = s[0]
    m = int(s[2])
    arr = list(s[4:].split())
    d[x] = arr

s = sys.stdin.readline().rstrip()
ans = "yes"

for i in range(len(s) - 1):
    if s[i] in d:
        if s[i + 1] in d[s[i]]:
            continue
        else:
            ans = "no"
            break

print(ans)