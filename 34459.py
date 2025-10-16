import sys


N = int(sys.stdin.readline())

for _ in range(N):
    P = int(sys.stdin.readline())

    if P <= 5:
        print("MIT time")
    else:
        num, cnt = 25, 2
        while True:
            if P <= num:
                break

            num *= 5
            cnt += 1

        print("MIT^%d time" %cnt)