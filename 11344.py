import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    sys.stdin.readline()
    N = int(sys.stdin.readline().rstrip())
    B, res = [], []
    change, maxLen = 0, 0
    for _ in range(N):
        arr = list(sys.stdin.readline().rstrip().split())
        money = int(arr[1])

        if arr[1] == '15':
            change += 1
        else:
            while change > 0 and len(B) > 0:
                change -= 1
                B.pop(0)
            if change > 0:
                change -= 1
                continue
            B.append(arr[0])
            if len(B) > maxLen:
                maxLen = len(B)
                res = B[:]

    if maxLen == 0:
        print("Line B stayed empty.")
    else:
        for i in res:
            print(i, end=' ')
        print()