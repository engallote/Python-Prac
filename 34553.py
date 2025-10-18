import sys


S = sys.stdin.readline().rstrip()
p, score, cnt = '.', 0, 0

for i in S:
    if p == '.' or p < i:
        cnt += 1
        score += cnt
    else:
        cnt = 1
        score += cnt

    p = i

print(score)