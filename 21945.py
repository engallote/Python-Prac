import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

res = 0
for i in arr:
    ch = str(i)

    l, r, flag = 0, len(ch) - 1, True

    while l <= r:
        if ch[l] == ch[r]:
            l += 1
            r -= 1
        else:
            flag = False
            break

    if flag:
        res += i

print(res)