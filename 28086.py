import sys

st = sys.stdin.readline()
num1, num2, idx, op = 0, 0, 0, '+'
if '+' in st:
    idx = st.find('+')
elif '/' in st:
    idx = st.find('/')
    op = '/'
elif '*' in st:
    idx = st.find('*')
    op = '*'
else:
    idx = st.find('-')
    if idx == 0:
        idx = st.find('-', 1)
    op = '-'


num1 = int(st[0:idx], 8)
num2 = int(st[idx + 1:], 8)
res = 0

if op == '+':
    res = oct(num1 + num2)
elif op == '-':
    res = oct(num1 - num2)
elif op == '*':
    res = oct(num1 * num2)
else:
    if num2 == 0:
        res = "invalid"
    else:
        res = oct(num1 // num2)

if res == "invalid":
    print(res)
elif res[0] == '-':
    print('-', end='')
    print(res[3:])
else:
    print(res[2:])