import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = int(N / 2)

ans = "no"
for i in range(k):
    a, b = arr[:i + 1], arr[N - i - 1:]
    print(a, b)
    if a == b:
        ans = "yes"
        break

print(ans)