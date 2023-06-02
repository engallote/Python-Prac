import sys

N = int(sys.stdin.readline())
d = {'@': 'a', '[': 'c', '!': 'i', ';': 'j', '^': 'n', '0': 'o', '7': 't'}
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    res, tmp = [], []
    cnt = 0
    idx = 0

    while idx < len(s):
        if s[idx] in d:
            res.append(d[s[idx]])
            cnt += 1
            idx += 1
        elif idx + 1 < len(s) and s[idx] == '\\' and s[idx + 1] == '\'':
            res.append('v')
            cnt += 1
            idx += 2
        elif idx + 2 < len(s) and s[idx] == '\\' and s[idx + 1] == '\\' and s[idx + 2] == '\'':
            res.append('w')
            cnt += 1
            idx += 3
        else:
            res.append(s[idx])
            idx += 1

    if cnt >= len(res) / 2.0:
        print("I don't understand")
    else:
        print(''.join(res))