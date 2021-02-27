import sys

N = int(sys.stdin.readline())
res = ""
for _ in range(N):
    K = int(sys.stdin.readline())
    name = sys.stdin.readline().rstrip()
    s, p = False, False
    for _ in range(K):
        menu = sys.stdin.readline().rstrip()
        if menu == "pea soup":
            s = True
        elif menu == "pancakes":
            p = True

    if s and p and len(res) == 0:
        res = name

if len(res) == 0:
    print("Anywhere is fine I guess")
else:
    print(res)