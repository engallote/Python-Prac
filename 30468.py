import sys

STR, DEX, INT, LUK, N = map(int, sys.stdin.readline().split())
a = STR + DEX + INT + LUK
cnt = 0
while True:
    if (a + cnt) // 4 >= N:
        break

    cnt += 1

print(cnt)