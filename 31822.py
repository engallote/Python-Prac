import sys


code = sys.stdin.readline()
N = int(sys.stdin.readline())

res = 0
for _ in range(N):
    sub = sys.stdin.readline()

    if code[:5] == sub[:5]:
        res += 1

print(res)