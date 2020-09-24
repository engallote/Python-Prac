def solve(cnt, start, s):
    if cnt == M:
        arr.add(s.strip())
        return
    for i in range(start, N + 1):
        solve(cnt + 1, i + 1, s + " " + str(i))


N, M = map(int, input().split())
arr = set()

solve(0, 1, "")

res = list(arr)
res.sort()

for i in res:
    print(i)