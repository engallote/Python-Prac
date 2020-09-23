import sys

N = int(sys.stdin.readline().rstrip())
num = N
cnt = 0

while True:
    num = num % 10 * 10 + (num//10 + num % 10) % 10
    cnt += 1
    if num == N:
        break

print(cnt)
