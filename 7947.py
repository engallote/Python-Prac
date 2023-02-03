import sys
import decimal

N = int(sys.stdin.readline())

for _ in range(N):
    r, g, b = 0, 0, 0
    for _ in range(10):
        a, bl, c = map(int, sys.stdin.readline().split())
        r += a
        g += bl
        b += c

    r /= 10
    g /= 10
    b /= 10

    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP

    print(round(decimal.Decimal(r), 0), round(decimal.Decimal(g), 0), round(decimal.Decimal(b), 0))