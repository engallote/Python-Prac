import sys


N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
al, ao = arr.count('L'), arr.count('O')
l, o, res = 0, 0, -1

for i in range(N):
    if arr[i] == 'L':
        l += 1
    else:
        o += 1

    if l != al - l and o != ao - o:
        if al - l == 0 and ao - o == 0:
            continue
        res = i + 1
        break

print(res)