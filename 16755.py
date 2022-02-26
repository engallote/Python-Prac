import sys

st = list(sys.stdin.readline().rstrip())
word = ['H', 'O', 'N', 'I']
res, idx = 0, 0
for i in range(len(st)):
    if st[i] == word[idx]:
        idx += 1
        if idx == 4:
            res += 1
            idx = 0

print(res)