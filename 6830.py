import sys


name, temp = "", 10000000
while True:
    N, M = sys.stdin.readline().rstrip().split()

    if temp > int(M):
        name = N
        temp = int(M)

    if N == "Waterloo":
        break

print(name)