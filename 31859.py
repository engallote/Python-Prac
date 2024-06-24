import sys

N, S = sys.stdin.readline().split()

s, cnt = [], 0
for i in S:
    if i in s:
        cnt += 1
    else:
        s.append(i)

s.append(str(cnt + 4))
s.insert(0, str(int(N) + 1906))
tmp = ''.join(s)

print('smupc_', end='')
print(tmp[::-1])