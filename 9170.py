import sys

while True:
    try:
        N = sys.stdin.readline()
        print(eval(N))
    except:
        break