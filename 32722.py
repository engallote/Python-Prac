import sys


arr1, arr2 = [1, 6, 2], [3, 8, 5]
ans = "JAH"
for i in range(3):
    N = int(sys.stdin.readline())
    if arr1[i] != N and arr2[i] != N:
        ans = "EI"

print(ans)