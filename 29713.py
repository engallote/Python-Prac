import sys

N = int(sys.stdin.readline())
s = list(sys.stdin.readline().rstrip())
t = "BRONZESILVER"

cnt, idx, f = 0, 0, 0
while True:
    f = 0
    for i in range(N):
        if s[i] == t[idx]:
            s[i] = "."
            idx += 1
            f = 1
            break

    if idx == len(t):
        cnt += 1
        idx = 0

    if f == 0:
        break

print(cnt)