import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    st = sys.stdin.readline().rstrip()
    arr.append(st[::-1])

arr.sort()
print('\n'.join(arr))