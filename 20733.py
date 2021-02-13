import sys

s = sys.stdin.readline().rstrip()
length = len(s)

for i in range(1, length):
    if length % i == 0 and length // i == 3:
        a = s[0:i]
        b = s[i:i+i]
        c = s[i+i:length]

        if a == b or a == c:
            print(a)
        elif b == a or b == c:
            print(b)
        else:
            print(c)
        break