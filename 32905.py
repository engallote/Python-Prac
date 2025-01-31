import sys


N, M = map(int, sys.stdin.readline().split())
ans = "Yes"
for _ in range(N):
    arr = list(sys.stdin.readline().rstrip().split())
    r, a, c, i = 0, 0, 0, 0
    for j in arr:
        if j == 'R':
            r += 1
        elif j == 'A':
            a += 1
        elif j == 'C':
            c += 1
        elif j == 'I':
            i += 1

    if a != 1:
        ans = "No"

print(ans)