import sys


N = int(sys.stdin.readline())

prime, chk = [], [False for _ in range(350000)]
chk[0] = chk[1] = True
prime.append(0)
for i in range(2, 350000):
    if chk[i]:
        continue
    prime.append(i)

    for j in range(i + i, 350000, i):
        chk[j] = True

arr = []
for i in range(len(prime)):
    if chk[i]:
        continue
    arr.append(prime[i])

for _ in range(N):
    x = int(sys.stdin.readline()) - 1
    print(arr[x])