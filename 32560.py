import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
alp1, alp2 = [0 for _ in range(130)], [0 for _ in range(130)]

for i in s1:
    alp1[ord(i)] += 1

for i in s2:
    alp2[ord(i)] += 1

for i in range(97, 123):
    if alp1[i] == 0 and alp2[i] == 0:
        continue

    n = max(alp1[i], alp2[i])
    for _ in range(n):
        print(chr(i), end='')