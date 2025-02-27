import sys


N = sys.stdin.readline().rstrip()

print(N)
for k in range(1, 26):
    for i in range(len(N)):
        c = ord(N[i]) - k
        if c < 65:
            c = 91 - (65 - c)
        print(chr(c), end='')

    print()