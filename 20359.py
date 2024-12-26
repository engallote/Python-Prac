import sys


N = int(sys.stdin.readline())

for i in range(1, N + 1):
    if i % 2 == 0 or N % i != 0:
        continue

    num = -1
    for j in range(N):
        if 2 ** j > N:
            break
        if 2 ** j * i == N:
            num = j
            break

    if num != -1:
        print(i, num)
        break