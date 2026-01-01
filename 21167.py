import sys


while True:
    tmp = sys.stdin.readline().rstrip()
    if tmp == "":
        break

    R, S = map(float, tmp.split())
    res = ((R * (S + .16)) / .067) ** 0.5

    print(round(res))