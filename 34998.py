import sys

N = int(sys.stdin.readline())

for _ in range(N):
    X = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()
    s = s.replace("!", "10")

    if eval(s) >= 10:
        print("!")
    else:
        print(eval(s))