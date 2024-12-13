import sys


N, M = map(int, sys.stdin.readline().split())
sn, sm = str(N), str(M)
sumN, sumM = 0, 0

for i in sn:
    sumN += int(i)

for i in sm:
    sumM += int(i)

if len(sn) * sumN > len(sm) * sumM:
    print(1)
elif len(sn) * sumN < len(sm) * sumM:
    print(2)
else:
    print(0)