import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

a, b = 0, 0
for i in range(N):
    if s[i] == 'S':
        if t[i] == 'P':
            a += 1
        elif t[i] == 'R':
            b += 1
    elif s[i] == 'P':
        if t[i] == 'S':
            b += 1
        elif t[i] == 'R':
            a += 1
    else:
        if t[i] == 'S':
            a += 1
        elif t[i] == 'P':
            b += 1

print(a, b)