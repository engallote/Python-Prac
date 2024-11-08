import sys


N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())

for i in range(N):
    if i + 1 < N and arr[i] == arr[i + 1]:
        if arr[i] == 'j':
            arr[i] = 'J'
            arr[i + 1] = 'J'
        elif arr[i] == 'o':
            arr[i] = 'O'
            arr[i + 1] = 'O'
        else:
            arr[i] = 'I'
            arr[i + 1] = 'I'
    print(arr[i], end='')