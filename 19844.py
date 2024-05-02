import sys
import re


s = sys.stdin.readline().rstrip()
arr = re.split('[- ]', s)
word = ['c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu']
mo = ['a', 'e', 'i', 'o', 'u', 'h']
res = len(arr)

for i in arr:
    if '\'' in i:
        idx = i.index('\'')
        if i[0:idx] in word and i[idx + 1] in mo:
            res += 1

print(res)