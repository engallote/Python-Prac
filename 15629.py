import sys

N = int(sys.stdin.readline())
dic = {'ethiopia': 50, 'kenya': 50, 'tanzania': 50, 'botswana': 0, 'south-africa': 0, 'zambia': 50, 'zimbabwe': 30,
       'namibia': 140}

res, sa, pre = 0, 0, ''
for _ in range(N):
    cn = sys.stdin.readline().rstrip()
    if cn == 'south-africa':
        sa = 1

    if cn == 'namibia':
        if sa == 1:
            res += 40
            continue
        else:
            res += dic[cn]
            continue

    res += dic[cn]

    if (cn == 'zambia' and pre == 'zimbabwe') or (cn == 'zimbabwe' and pre == 'zambia'):
        res -= 30

    pre = cn

print(res)