import sys

chk = [False for _ in range(1000001)]
chk[0] = chk[1] = True
for i in range(2, 1000001):
    if chk[i]:
        continue

    for j in range(i + i, 1000001, i):
        chk[j] = True

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr2 = []

for i in arr:
    if not chk[i]:
        arr2.append(i)

if len(arr2) == 0:
    print(-1)
else:
    res = 1
    st = set()
    for i in arr2:
        if i in st:
            continue
        st.add(i)
        res *= i

    print(res)