import sys


N = int(sys.stdin.readline())
arr = [['.' for _ in range(21)] for _ in range(10)]

for _ in range(N):
    s = sys.stdin.readline().rstrip()

    row = s[0]
    col = int(s[1:])

    arr[ord(row) - 65][col] = 'o'

for i in range(10):
    for j in range(1, 21):
        print(arr[i][j], end='')
    print()