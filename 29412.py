import sys


g, gb, y, r, ry = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())

green, red, yellow = 0, 0, 0

while T > 0:
    if g <= T:
        green += g
        T -= g
    else:
        green += T
        break

    if gb <= T:
        green += gb // 2
        T -= gb
    else:
        green += T // 2
        break

    if y <= T:
        yellow += y
        T -= y
    else:
        yellow += T
        break

    if r <= T:
        red += r
        T -= r
    else:
        red += T
        break

    if ry <= T:
        red += ry
        yellow += ry
        T -= ry
    else:
        red += T
        yellow += T
        break

print(red, yellow, green)