import sys

Cu, Du = map(int, sys.stdin.readline().split())
Cd, Dd = map(int, sys.stdin.readline().split())
Cp, Dp = map(int, sys.stdin.readline().split())
H = int(sys.stdin.readline())

time = 0
while H > 0:
    if time % Cu == 0:
        H -= Du
    if time % Cd == 0:
        H -= Dd
    if time % Cp == 0:
        H -= Dp

    time += 1

print(time - 1)