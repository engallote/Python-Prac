import sys

N = int(sys.stdin.readline())

for _ in range(N):
    st = list(sys.stdin.readline().rstrip().upper())
    flag = True
    for i in range(len(st)):
        c = st[i]
        if c < 'A' or c > 'Z':
            continue
        flag = False
        for j in range(i + 1, len(st)):
            if (c == 'A' and st[j] == 'Z') or (c == 'Z' and st[j] == 'A'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'B' and st[j] == 'Y') or (c == 'Y' and st[j] == 'B'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'C' and st[j] == 'X') or (c == 'X' and st[j] == 'C'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'D' and st[j] == 'W') or (c == 'W' and st[j] == 'D'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'E' and st[j] == 'V') or (c == 'V' and st[j] == 'E'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'F' and st[j] == 'U') or (c == 'U' and st[j] == 'F'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'G' and st[j] == 'T') or (c == 'T' and st[j] == 'G'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'H' and st[j] == 'S') or (c == 'S' and st[j] == 'H'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'I' and st[j] == 'R') or (c == 'R' and st[j] == 'I'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'J' and st[j] == 'Q') or (c == 'Q' and st[j] == 'J'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'K' and st[j] == 'P') or (c == 'P' and st[j] == 'K'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'L' and st[j] == 'O') or (c == 'O' and st[j] == 'L'):
                flag = True
                st[j] = '.'
                break
            elif (c == 'M' and st[j] == 'N') or (c == 'N' and st[j] == 'M'):
                flag = True
                st[j] = '.'
                break
        if not flag:
            print("No")
            break
    if flag:
        print("Yes")