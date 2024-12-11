import sys


Y, M = map(int, sys.stdin.readline().split())
if Y == 0:
    print((M * 15) // 12, (M * 15) % 12)
elif Y == 1:
    print(15 + (M * 9) // 12, (M * 9) % 12)
else:
    Y -= 2
    print(15 + 9 + (Y * 4) + ((M * 4) // 12), (M * 4) % 12)