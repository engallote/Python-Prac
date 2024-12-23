import sys


N, K = map(int, sys.stdin.readline().split())
num, arr, a, b = 0, [], K % 10, K * 2 % 10
while True:
    if num == N:
        break

    num += 1
    if num % 10 == a or num % 10 == b:
        continue

    arr.append(num)

print(len(arr))
print(*arr)