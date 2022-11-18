import sys
from functools import reduce

t = 1
while True:
    str = sys.stdin.readline().rstrip()
    if str == 'Was it a cat I saw?':
        break

    for j in range(0, len(str), t + 1):
        print(str[j], end='')
    print()
    t += 1