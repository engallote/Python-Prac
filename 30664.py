import sys


while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    if N % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")