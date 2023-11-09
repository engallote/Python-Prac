import sys

N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip())
alp = [0 for _ in range(26)]
for i in range(N // 2):
    alp[ord(arr[i]) - 97] += 1

num = N % 2
for i in range(N // 2 + num, N):
    alp[ord(arr[i]) - 97] -= 1

# print(alp)
o = 0
for i in alp:
    if i != 0 and i % 2 != 0:
        o += 1

if N % 2 == 0:
    if o == 0:
        print("Yes")
    else:
        print("No")
else:
    if o == 0:
        print("Yes")
    else:
        print("No")