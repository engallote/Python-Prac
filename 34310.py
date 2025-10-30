import sys


N = int(sys.stdin.readline())
s, v, f = 0, 0, 0
for _ in range(N):
    who, go, num = sys.stdin.readline().rstrip().split()

    if go == "IN":
        if who == "STU":
            s += int(num)
        elif who == "FAC":
            f += int(num)
        else:
            v += int(num)
    else:
        if who == "STU":
            s -= int(num)
        elif who == "FAC":
            f -= int(num)
        else:
            v -= int(num)

if s + f + v > 0:
    print(s + f + v)
else:
    print("NO STRAGGLERS")