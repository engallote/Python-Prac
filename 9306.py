import sys

T = int(sys.stdin.readline().rstrip())

for i in range(1, T + 1):
    arr = []
    for _ in range(2):
        arr.append(sys.stdin.readline().rstrip())

    arr.reverse()
    print("Case %d: %s" %(i, ', '.join(arr)))