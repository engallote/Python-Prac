import sys


N = sys.stdin.readline().rstrip()

if len(N) <= 2:
    print("Incorrect")
else:
    if N[0] == 'i' and N[1] == 'o':
        f = -1
        for i in range(2, len(N)):
            if '0' <= N[i] <= '9':
                continue
            else:
                f = 1

        if f == 1:
            print("Incorrect")
        else:
            print("Correct")
    else:
        print("Incorrect")