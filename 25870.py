import sys


s = sys.stdin.readline().rstrip()
arr = [0 for _ in range(26)]

for i in s:
    arr[ord(i) - 97] += 1

o, e = 0, 0
for i in range(26):
    if arr[i] == 0:
        continue
    if arr[i] % 2 == 0:
        e += 1
    else:
        o += 1

if e == 0 and o > 0:
    print(1)
elif e > 0 and o == 0:
    print(0)
else:
    print(2)