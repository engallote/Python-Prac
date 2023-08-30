import sys


d = sys.stdin.readline().rstrip()

arr = []
for i in range(2):
    arr.append(list(sys.stdin.readline().rstrip()))

if d == 'S':
    if arr[0][1] == 'O' and arr[1][0] == 'P' and arr[0][0] == '.' and arr[1][1] == '.':
        print("T")
    elif arr[0][0] == 'I' and arr[1][1] == 'P' and arr[0][1] == '.' and arr[1][0] == '.':
        print("F")
    elif arr[0][0] == 'O' and arr[1][1] == 'P' and arr[0][1] == '.' and arr[1][0] == '.':
        print("Lz")
    else:
        print("?")
elif d == 'N':
    if arr[1][0] == 'O' and arr[0][1] == 'P' and arr[0][0] == '.' and arr[1][1] == '.':
        print("T")
    elif arr[1][1] == 'I' and arr[0][0] == 'P' and arr[0][1] == '.' and arr[1][0] == '.':
        print("F")
    elif arr[1][1] == 'O' and arr[0][0] == 'P' and arr[0][1] == '.' and arr[1][0] == '.':
        print("Lz")
    else:
        print("?")
elif d == 'E':
    if arr[0][0] == 'O' and arr[1][1] == 'P' and arr[0][1] == '.' and arr[1][0] == '.':
        print("T")
    elif arr[1][0] == 'I' and arr[0][1] == 'P' and arr[0][0] == '.' and arr[1][1] == '.':
        print("F")
    elif arr[1][0] == 'O' and arr[0][1] == 'P' and arr[0][0] == '.' and arr[1][1] == '.':
        print("Lz")
    else:
        print("?")
else:
    if arr[1][1] == 'O' and arr[0][0] == 'P' and arr[0][1] == '.' and arr[1][0] == '.':
        print("T")
    elif arr[0][1] == 'I' and arr[1][0] == 'P' and arr[0][0] == '.' and arr[1][1] == '.':
        print("F")
    elif arr[0][1] == 'O' and arr[1][0] == 'P' and arr[0][0] == '.' and arr[1][1] == '.':
        print("Lz")
    else:
        print("?")