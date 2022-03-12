import sys

N = int(sys.stdin.readline())
arr = [0] * N

for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().rstrip().split()))

chk = [False for _ in range(N + 1)]
for i in range(1, 5):
    mx, idx = -1, 0
    for j in range(0, N):
        if mx < arr[j][i] and not chk[arr[j][0]]:
            mx = arr[j][i]
            idx = arr[j][0]
        elif mx == arr[j][i] and idx > arr[j][0] and not chk[arr[j][0]]:
            idx = arr[j][0]

    chk[idx] = True
    print(idx, end=' ')