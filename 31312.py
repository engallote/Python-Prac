import sys


N, a, b = map(int, sys.stdin.readline().split())

mi, ma = False, False
for _ in range(N - 1):
    num = int(sys.stdin.readline())

    if num == a:
        mi = True
    elif num == b:
        ma = True

if mi and ma:
    for i in range(a, b + 1):
        print(i)
elif not mi and ma:
    print(a)
elif mi and not ma:
    print(b)
else:
    print(-1)