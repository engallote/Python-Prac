import sys


N = int(sys.stdin.readline())
m, j, mc, jc = 0, 0, 0, 0

for i in range(N):
    a, b = sys.stdin.readline().split()

    if a == "M":
        m += int(b)
        mc += 1
    else:
        j += int(b)
        jc += 1

if mc == 0:
    mc = 1
if jc == 0:
    jc = 1

if m / mc > j / jc:
    print("M")
elif m / mc < j / jc:
    print("J")
else:
    print("V")