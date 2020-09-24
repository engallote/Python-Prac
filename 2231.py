N = int(input())
res = 0
for i in range(max(1, N - 9 * len(str(N))), N):
    if i + sum(list(map(int, str(i)))) == N:
        res = i
        break

print(res)