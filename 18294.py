import sys

N = int(sys.stdin.readline())
dic = {}
name = "NONE"

for _ in range(N):
    animal = sys.stdin.readline().rstrip()
    if animal in dic:
        dic[animal] += 1
    else:
        dic[animal] = 1

for k, v in dic.items():
    if v > N - v:
        name = k
        break

print(name)