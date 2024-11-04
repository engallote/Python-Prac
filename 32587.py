import sys


N = int(sys.stdin.readline())
arr1 = list(sys.stdin.readline())
arr2 = list(sys.stdin.readline())
v, l = 0, 0

for i in range(N):
    if arr1[i] == 'S':
        if arr2[i] == 'P':
            v += 1
        elif arr2[i] == 'R':
            l += 1
    elif arr1[i] == 'R':
        if arr2[i] == 'P':
            l += 1
        elif arr2[i] == 'S':
            v += 1
    else:
        if arr2[i] == 'R':
            v += 1
        elif arr2[i] == 'S':
            l += 1

if v > l:
    print("victory")
elif v < l:
    print("defeat")
else:
    print("draw")