import sys


N = int(sys.stdin.readline())

for _ in range(N):
    s = list(sys.stdin.readline().rstrip())
    rev = reversed(s)
    rev = list(rev)

    tmp = []
    flag = False
    for i in range(len(s)):
        if s[i] == rev[0]:
            idx = 0
            flag = True
            for j in range(i, len(s)):
                if s[j] == rev[idx]:
                    idx += 1
                else:
                    flag = False
                    break
            if flag:
                for j in range(len(rev)):
                    tmp.append(rev[j])
        if flag:
            break
        tmp.append(s[i])

    if not flag:
        for j in rev:
            tmp.append(j)

    print(''.join(tmp))
