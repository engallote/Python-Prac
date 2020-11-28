import sys

N = sys.stdin.readline().rstrip()

for num in range(0, 10):
    cnt, res = 1, 0
    for i in N:
        if i == '*':
            res += num * cnt
        else:
            res += int(i) * cnt

        if cnt == 1:
            cnt = 3
        else:
            cnt = 1

    if res % 10 == 0:
        print(num)
        break