import sys

N = int(sys.stdin.readline())
arr = list(sys.stdin.readline())

B = arr.count('B')
S = arr.count('S')
A = arr.count('A')

res = [('B', B), ('S', S), ('A', A)]
res.sort(key=lambda x: -x[1])

if res[0][1] == res[2][1]:
    print("SCU")
else:
    pre = res[0][1]
    for i in res:
        if i[1] == pre:
            print(i[0], end='')
        else:
            break