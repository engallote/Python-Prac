import sys


N = int(sys.stdin.readline())
chk = []

for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'all':
        chk = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    elif order[0] == 'empty':
        chk = []
    elif order[0] == 'add':
        if order[1] in chk:
            continue
        chk.append(order[1])
    elif order[0] == 'remove':
        if order[1] in chk:
            chk.remove(order[1])
    elif order[0] == 'check':
        print(1 if order[1] in chk else 0)
    else:
        if order[1] in chk:
            chk.remove(order[1])
        else:
            chk.append(order[1])