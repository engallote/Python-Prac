import sys


cnt = 0
while True:
    s = sys.stdin.readline().rstrip()

    if s == "":
        break

    cnt += 1

print(cnt)