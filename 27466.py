import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().rstrip())
arr.reverse()
s = ''.join(arr)

res = []
flag = False
idx = -1
ans = ""
for i in range(len(s)):
    if s[i] not in ('A', 'E', 'I', 'O', 'U'):
        flag = True
        idx1 = s.find('A', i + 1)

        if idx1 == -1:
            flag = False
            break

        idx2 = s.find('A', idx1 + 1)

        if idx2 == -1:
            flag = False
            break

        res.append(s[i])
        res.append(s[idx1])
        res.append(s[idx2])

        end = M - 2
        if idx2 + end > len(s):
            flag = False
            break
        ans = s[idx2 + 1:idx2 + end]
        break

    if flag:
        break

if flag and len(ans) + 3 == M:
    res.reverse()

    res.insert(0, ans[::-1])
    print("YES")
    print(''.join(res))
else:
    print("NO")