import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    num, res = map(int, sys.stdin.readline().split())

    q = deque()
    q.append((num, ""))
    chk = [False for _ in range(10000)]

    while len(q):
        x, path = q.popleft()

        if x == res:
            print(path)
            break

        #D
        if not chk[x * 2 % 10000]:
            chk[x * 2 % 10000] = True
            q.append((x * 2 % 10000, path + "D"))
        #S
        tmp = x - 1
        if tmp < 0 :
            tmp = 9999
        if not chk[tmp]:
            chk[tmp] = True
            q.append((tmp, path + "S"))
        #L
        tmp = (x % 1000) * 10 + x // 1000
        if not chk[int(tmp)]:
            chk[int(tmp)] = True
            q.append((int(tmp), path + "L"))
        #R
        tmp = (x % 10) * 1000 + x // 10
        if not chk[int(tmp)]:
            chk[int(tmp)] = True
            q.append((int(tmp), path + "R"))