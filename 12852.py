import sys
from collections import deque

N = int(sys.stdin.readline())
chk = set()
arr = [0 for _ in range(N+1)]
q = deque()
q.append((N, 0))

while q:
    x, cnt = q.popleft()

    if x == 1:
        print(cnt)
        res = []
        idx = 1
        while arr[idx] != 0:
            res.append(str(arr[idx]))
            idx = arr[idx]
        res.reverse()
        res.append("1")
        print(" ".join(res))
        break

    if x % 2 == 0 and int(x / 2) not in chk:
        chk.add(int(x / 2))
        arr[int(x / 2)] = x
        q.append((int(x / 2), cnt + 1))
    if x % 3 == 0 and int(x / 3) not in chk:
        chk.add(int(x / 3))
        arr[int(x / 3)] = x
        q.append((int(x / 3), cnt + 1))
    if x - 1 >= 1 and x - 1 not in chk:
        chk.add(x - 1)
        arr[int(x - 1)] = x
        q.append((x - 1, cnt + 1))