import sys


s = input()
one = ['`','1','2','3','4','5','6','7','8','9','0', '-', '=']
two = ['Q','W','E','R','T','Y','U','I','O','P','[',']', '\\']
thr = ['A','S','D','F','G','H','J','K','L',';','\'']
res = []

for i in s:
    if i == ' ':
        res.append('5')
    elif i in one:
        res.append('1')
    elif i in two:
        res.append('2')
    elif i in thr:
        res.append('3')
    else:
        res.append('4')

print(''.join(res))
