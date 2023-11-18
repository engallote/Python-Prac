import sys

N, cost = map(int, sys.stdin.readline().split())

dic = {"bedroom":0, "bathroom":0, "kitchen":0, "balcony":0, "other":0}
s, d = 0, 0
for _ in range(N):
    num, room = sys.stdin.readline().split()

    dic[room] += int(num)
    s += int(num)

    if room == "balcony":
        d += int(num)

print(s)
print(dic["bedroom"])
print(round((s - d / 2) * cost, 1))