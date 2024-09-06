import sys


N = int(sys.stdin.readline())
d, m = N // 8, N % 8

if m == 0:
    num = d
else:
    num = d + 1

alp = N - 8 * d
if alp == 0:
    alp = 8

print(chr(alp + ord('a') - 1), end='')
print(num)