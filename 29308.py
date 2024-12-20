import sys


N = int(sys.stdin.readline())
mx, n = -100000, ""
for _ in range(N):
    salary, name, country = sys.stdin.readline().split()

    if country != "Russia":
        continue

    if int(salary) > mx:
        mx = int(salary)
        n = name

print(n)