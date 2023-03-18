import sys

N = int(sys.stdin.readline())

all, check, num = 0, 0, 0.0
for i in range(N):
    all = ''

    while True:
        s = sys.stdin.readline()

        if s == '\n':
            break
        else:
            all += s.rstrip()

    allLen = len(all)
    check = all.count('#')

    if check == 0:
        num = 100
    else:
        num = round(100 - check / allLen * 100, 1)

    if str(num)[-1] == '0':
        num = int(num)
    print(f"Efficiency ratio is {num}%.")