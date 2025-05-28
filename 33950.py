import sys


N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    arr = []

    for i in range(len(s)):
        if i - 1 >= 0 and s[i] == 'O' and s[i-1] == 'P':
            arr.append('H')
            arr.append(s[i])
        else:
            arr.append(s[i])

    print(*arr, sep='')