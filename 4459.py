import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline())
for _ in range(M):
    num = int(sys.stdin.readline())

    if num > len(arr) or num <= 0:
        print("Rule %d: No such rule" %num)
    else:
        print("Rule %d: %s" % (num, ''.join(arr[num - 1])))
