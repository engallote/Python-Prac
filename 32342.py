import sys


Q = int(sys.stdin.readline())

for _ in range(Q):
    res = 0
    s = sys.stdin.readline().rstrip()

    for i in range(len(s)):
        if i + 2 >= len(s):
            break

        if s[i] == "W" and s[i+1] == "O" and s[i+2] == "W":
            res += 1

    print(res)