import sys

T, N = map(int, sys.stdin.readline().split())
dic = {'Mon' : 1, 'Tue' : 2, 'Wed' : 3, 'Thu' : 4, 'Fri' : 5}
s = 0
for _ in range(N):
    arr = list(sys.stdin.readline().split())
    d1, t1, d2, t2 = arr[0], int(arr[1]), arr[2], int(arr[3])

    if d1 == d2:
        s += t2 - t1
    else:
        s += 24 * abs(dic[d1] - dic[d2]) - (t1 - t2)

if s >= T:
    print(0)
elif s + 48 < T:
    print(-1)
else:
    print(T - s)