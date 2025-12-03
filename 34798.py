import sys


h1, m1 = map(int, sys.stdin.readline().split(":"))
h2, m2 = map(int, sys.stdin.readline().split(":"))

if h1 == h2:
    if m1 > m2:
        print("NO")
    else:
        print("YES")
elif h1 < h2:
    print("YES")
else:
    print("NO")