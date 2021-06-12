import sys

N = int(sys.stdin.readline())

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())
res = []

for i in range(N):
    if a[i] == b[i]:
        if a[i] == 'R':
            res.append('P')
        elif a[i] == 'P':
            res.append('S')
        else:
            res.append('R')
    else:
        if a[i] == 'R':
            if b[i] == 'S':
                res.append(a[i])
            else:
                res.append(b[i])
        elif a[i] == 'P':
            if b[i] == 'S':
                res.append(b[i])
            else:
                res.append(a[i])
        else:
            if b[i] == 'P':
                res.append(a[i])
            else:
                res.append(b[i])

print(''.join(res))