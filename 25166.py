import sys

S, M = map(int, sys.stdin.readline().split())
arr = []

for i in range(9, 0, -1):
    if M >= 2 ** i:
        M -= 2 ** i
        arr.append(2**i)

if M == 1:
    arr.append(1)

ans = "Impossible"
for i in range(9, 0, -1):
    if S >= 2 ** i:
        S -= 2 ** i
    if S == 0:
        ans = "No thanks"
        break

if S == 1:
    ans = "No thanks"
    S = 0
elif S > 1:
    S -= 1

if S > 0:
    for i in arr:
        if i <= S:
            S -= i
        if S == 0:
            ans = "Thanks"
            break

print(ans)