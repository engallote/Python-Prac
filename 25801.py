import sys

s = sys.stdin.readline().rstrip()
alp = [0 for _ in range(26)]
odd, even = 0, 0

for i in s:
    alp[ord(i) - 97] += 1

for i in range(26):
    if alp[i] == 0:
        continue

    if alp[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if even == 0:
    print(1)
elif odd == 0:
    print(0)
else:
    print("0/1")