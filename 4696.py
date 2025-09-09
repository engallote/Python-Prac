import sys


while True:
    n = float(sys.stdin.readline())
    if n == 0:
        break

    wife = n
    sack = n * n
    cat = n * n * n
    kitten = n * n * n * n

    res = wife + sack + cat + kitten + 1
    print("%.2f" %res)