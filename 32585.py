import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(N+1)]
jump, num = 3, 3

arr[1] = 1

for i in range(2, N + 1):
    arr[i] = arr[i - 1] + jump
    jump += num
    num += 1

print(arr[N])