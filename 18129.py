import sys

st, K = sys.stdin.readline().split()
arr = list(st.upper())
K = int(K)
s = set()
pre, cnt = '.', 0
res = []
for i in arr:
    if pre == i:
        cnt += 1
    else:
        if pre != '.' and pre not in s:
            if cnt >= K:
                res.append('1')
            else:
                res.append('0')
            s.add(pre)
        cnt = 1

    pre = i

if pre not in s:
    if cnt >= K:
        res.append('1')
    else:
        res.append('0')

print(''.join(res))