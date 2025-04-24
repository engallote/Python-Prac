import sys


key = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip().split())
res = 0

for i in range(N):
    s = arr[i]

    for j in range(len(s)):
        if s[j] == key[0]:
            idx = 0
            for k in range(j, len(s)):
                if s[k] == key[idx]:
                    idx += 1
                    if idx == len(key):
                        res += 1
                        break
                else:
                    break

print(res)