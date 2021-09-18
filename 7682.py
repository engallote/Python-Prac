import sys

arr, map = [], [['.','.','.'], ['.','.','.'], ['.','.','.']]

while True :
    st = sys.stdin.readline().rstrip()

    if st == 'end':
        break

    arr = list(st)

    idx, x, o, e = 0, 0, 0, 0

    for i in range(0, 3):
        for j in range(0, 3):
            map[i][j] = arr[idx]
            if arr[idx] == 'X':
                x += 1
            elif arr[idx] == 'O':
                o += 1
            else:
                e += 1
            idx += 1

    xw, ow = False, False

    for i in range(0, 3):
        pre, cnt = '!', 0
        #가로 검사
        if map[i][0] == map[i][1] == map[i][2]:
            if map[i][0] == 'X':
                xw += 1
            elif map[i][0] == 'O':
                ow += 1
        #세로 검사
        if map[0][i] == map[1][i] == map[2][i]:
            if map[0][i] == 'X':
                xw = True
            elif map[0][i] == 'O':
                ow = True

    # 대각선
    if map[0][0] == map[1][1] == map[2][2]:
        if map[0][0] == 'X':
            xw = True
        elif map[0][0] == 'O':
            ow = True
    if map[0][2] == map[1][1] == map[2][0]:
        if map[0][2] == 'X':
            xw = True
        elif map[0][2] == 'O':
            ow = True

    # print(xw, ow)
    if xw and not ow and x == o + 1:
        print('valid')
    elif not xw and ow and x == o:
        print('valid')
    elif not xw and not ow and x == 5 and o == 4:
        print('valid')
    else:
        print('invalid')