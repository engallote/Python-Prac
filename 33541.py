import sys


N = int(sys.stdin.readline())
e = 0
for i in range(N + 1, 9999):
    a, b = i // 100, i % 100

    if (a + b) ** 2 == i:
        e = 1
        print(i)
        break

if e == 0:
    print(-1)