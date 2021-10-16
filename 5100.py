import sys


while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    arr = [0 for _ in range(5)]

    for _ in range(N):
        size = sys.stdin.readline().rstrip()
        if size.isalpha():
            if size == "M" or size == "L":
                arr[0] += 1
            elif size == "S":
                arr[3] += 1
            else:
                arr[4] += 1
        else:
            if int(size) >= 12:
                arr[1] += 1
            elif int(size) < 12:
                arr[2] += 1

    print(' '.join(str(x) for x in arr))