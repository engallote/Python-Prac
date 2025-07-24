import sys


pre = ""
while True:
    N = sys.stdin.readline().rstrip()
    if N == "99999":
        break

    dir, go = "", 0
    if (int(N[0]) + int(N[1])) % 2 != 0:
        dir = "left"
    else:
        if int(N[0]) + int(N[1]) != 0:
            dir = "right"
        else:
            dir = pre

    go = int(N[2:])
    print(dir, go)

    pre = dir