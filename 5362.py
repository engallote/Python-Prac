import sys


while True:
    s = sys.stdin.readline().rstrip()

    if s == "":
        break

    s = s.replace("iiing", "th")
    print(s)