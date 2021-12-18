import sys


N = int(sys.stdin.readline())

e, o = False, False

for i in range(1, 101):
    s = 0
    for j in range(N):
        s += i + j
    if s % 2 == 0:
        e = True
    else:
        o = True

if e and o:
    print("Either")
elif e:
    print("Even")
else:
    print("Odd")