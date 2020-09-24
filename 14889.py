import sys
from itertools import combinations

def calc(num):
    ret = 0
    for i in num:
        for j in num:
            ret += arr[i][j]
    return ret


N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

comb = list(combinations([i for i in range(N)], N // 2))
half = len(comb) // 2
start = comb[:half]
link = list(reversed(comb[half:]))

res = 10000000000
for i in range(len(start)):
    res = min(res, abs(calc(start[i]) - calc(link[i])))

print(res)