import sys

N = int(sys.stdin.readline())

res = ''
for _ in range(N):
    n = sys.stdin.readline().rstrip()

    if 'S' in n:
        res = n

print(res)