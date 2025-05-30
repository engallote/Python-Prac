import sys


s = sys.stdin.readline().rstrip()
arr = ['a', 'e', 'i', 'o', 'u']
p = 0
if s[-1] != 'n' and s[-1] != 's' and s[-1] not in arr:
    for i in range(len(s) - 1, -1, -1):
        if s[i] in arr:
            print(i + 1)
            p = 1
            break
elif s[-1] == 'n' or s[-1] == 's' or s[-1] in arr:
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] in arr:
            cnt += 1
            if cnt == 2:
                print(i + 1)
                p = 1
                break

if p == 0:
    print(-1)