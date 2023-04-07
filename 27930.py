import sys


str = sys.stdin.readline().rstrip()
yon, kor = ['Y','O','N','S','E','I'], ['K','O','R','E','A']
ydx, kdx, who = 0, 0, -1

for i in str:
    if yon[ydx] == i:
        ydx += 1
        if ydx == len(yon):
            who = 0
            break
    if kor[kdx] == i:
        kdx += 1
        if kdx == len(kor):
            who = 1
            break

if who == 0:
    print("YONSEI")
else:
    print("KOREA")

