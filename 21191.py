import sys

N = int(sys.stdin.readline())

arr, rev = [sys.stdin.readline().rstrip() for _ in range(N)], []

for j in range(N):
    tmp = ''
    for i in range(N):
        tmp += arr[i][j]
    rev.append(tmp)

flag = True

for i in range(N):
    if arr[i].count('B') != arr[i].count('W') or rev[i].count('B') != rev[i].count('W'):
        flag = False
        break
    if 'WWW' in arr[i] or 'BBB' in arr[i] or 'WWW' in rev[i] or 'BBB' in rev[i]:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)