import sys

N = int(sys.stdin.readline())

cost, name = 0, ""
for _ in range(N):
    st = sys.stdin.readline()
    num = int(sys.stdin.readline())

    if num > cost:
        cost = num
        name = st

print(name)