import sys

B = int(sys.stdin.readline())

num, A = 10, 0
while True:
    tmp = B - num

    if int(tmp * 0.1) == num:
        A = tmp
        break

    num += 10

print(A)