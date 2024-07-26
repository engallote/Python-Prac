import sys


N = sys.stdin.readline()

mo, y = 0, 0
for i in N:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        mo += 1
    elif i == 'y':
        y += 1

print(mo, mo + y)