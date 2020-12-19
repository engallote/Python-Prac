import sys


win = 0
for _ in range(6):
    game = sys.stdin.readline()

    if game[0] == 'W':
        win += 1

if 5 <= win <= 6:
    print(1)
elif 3 <= win <= 4:
    print(2)
elif 1 <= win <= 2:
    print(3)
else:
    print(-1)