import sys

N = int(sys.stdin.readline().rstrip())
mp = [['.' for _ in range(8)] for _ in range(8)]
arr = ['.' for _ in range(65)]
sw, cnt = 1, 1

for i in range(8):
    for j in range(8):

        if sw == 1:
            mp[i][j] = 'B'
            arr[cnt] = 'B'
        else:
            mp[i][j] = 'W'
            arr[cnt] = 'W'
        if j != 7:
            sw *= -1
        cnt += 1

for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()

    A, B = '.', arr[int(b)]
    if a[0] == 'A':
        A = mp[0][int(a[1]) - 1]
    elif a[0] == 'B':
        A = mp[1][int(a[1]) - 1]
    elif a[0] == 'C':
        A = mp[2][int(a[1]) - 1]
    elif a[0] == 'D':
        A = mp[3][int(a[1]) - 1]
    elif a[0] == 'E':
        A = mp[4][int(a[1]) - 1]
    elif a[0] == 'F':
        A = mp[5][int(a[1]) - 1]
    elif a[0] == 'G':
        A = mp[6][int(a[1]) - 1]
    else:
        A = mp[7][int(a[1]) - 1]

    if A == B:
        print("YES")
    else:
        print("NO")