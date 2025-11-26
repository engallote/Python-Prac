import sys


N = int(sys.stdin.readline())
all, p = 0, 0
for _ in range(N):
    s = sys.stdin.readline().rstrip()

    if s[0] == "A":
        all += 4
        if s[1] == "1":
            p += 0.05
        elif s[1] == "2":
            p += 0.025
    elif s[0] == "B":
        all += 3
        if s[1] == "1":
            p += 0.05
        elif s[1] == "2":
            p += 0.025
    elif s[0] == "C":
        all += 2
        if s[1] == "1":
            p += 0.05
        elif s[1] == "2":
            p += 0.025
    elif s[0] == "D":
        all += 1

print(all / N + p)