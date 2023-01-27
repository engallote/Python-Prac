import sys

N = int(sys.stdin.readline())
dic = dict()

for i in range(N):
    s = sys.stdin.readline().rstrip()
    s = s.removeprefix("http://")
    flag = False

    start, end = 0, len(s)
    for j in range(0, len(s)):
        if s[j] == '.':
            start = j + 1
        elif s[j] == '/':
            end = j
            break

    if s[start:end] in dic:
        dic[s[start:end]] += 1
    else:
        dic[s[start:end]] = 1

num = max(dic.values())
print(num)

for i in dic:
    if dic[i] == num:
        print(i, end=' ')
